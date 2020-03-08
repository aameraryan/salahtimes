import datetime
import time

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse_lazy, reverse
from django.utils import timezone

from localities.models import Area


class Masjid(models.Model):

    area = models.ForeignKey(Area, on_delete=models.PROTECT)

    name = models.CharField(max_length=256)
    address = models.TextField(blank=True)
    extra_info = models.TextField(blank=True)

    fajar = models.TimeField()
    zuhar = models.TimeField()
    asar = models.TimeField()
    maghrib = models.TimeField()
    isha = models.TimeField()
    juma = models.TimeField()

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(verbose_name="Last Updated On", auto_now=True)

    def __str__(self):
        return self.name

    def get_address_display(self):
        return "{}".format(self.address)

    class Meta:
        verbose_name = "Masjid"
        verbose_name_plural = "Masajid"

    @property
    def get_update_url(self):
        return reverse_lazy("masjids:update", kwargs={"id": self.id})

    @property
    def get_admins_text(self):
        text = ""
        all_admins = self.masjidstaff_set.all()
        if all_admins.exists():
            for admin in all_admins:
                text += "{} - {} - {}".format(admin.name, admin.phone, admin.created_on)
        else:
            text = "no admins"
        return text

    @property
    def get_staff_count(self):
        return self.masjidstaff_set.all().count()

    def get_staff_count_admin(self):
        return self.get_staff_count

    get_staff_count_admin.short_description = "No. of Admins"

    @property
    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return settings.SITE_DOMAIN + str(
            reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,)))

    @property
    def get_last_updated_text(self):
        last_updated = (timezone.now()-self.updated_on).days
        if last_updated == 0:
            text = "Today"
        elif last_updated == 1:
            text = "Yesterday"
        elif last_updated >= 30:
            text = "{} months ago".format(last_updated//30)
        else:
            text = "{} days ago".format(last_updated)
        return text

    def get_last_updated_text_admin(self):
        return self.get_last_updated_text

    get_last_updated_text_admin.short_description = "Last Updated"

    @property
    def get_email_message_details(self):
        message = """

        Masjid Details : 

            Name : {0},
            Address : {1},
            Fajar : {2},
            Zuhar : {3},
            Asar : {4},
            Maghrib : {5}, 
            Isha : {6}, 
            Juma : {7}, 

            url : {8}, 
                  """.format(self.name, self.address, self.fajar.strftime("%g:%h %A"), self.zuhar, self.asar,
                             self.maghrib, self.isha, self.juma, self.get_admin_url)
        return message


def validate_times(instance, sender, *args, **kwargs):
    am_times = ['fajar']
    pm_times = ['zuhar', 'asar', 'maghrib', 'isha', "juma"]
    is_changed = False
    for namaz in am_times:
        namaz_attr = getattr(instance, namaz)
        if namaz_attr > datetime.time(12, 0, 0):
            new_time = (datetime.datetime.combine(datetime.date(1, 1, 1), namaz_attr) - datetime.timedelta(hours=12)).time()
            setattr(instance, namaz, new_time)
            is_changed = True
    for namaz in pm_times:
        namaz_attr = getattr(instance, namaz)
        if namaz_attr < datetime.time(12, 0, 0):
            new_time = (datetime.datetime.combine(datetime.date(1, 1, 1), namaz_attr) + datetime.timedelta(hours=12)).time()
            setattr(instance, namaz, new_time)
            is_changed = True
    if is_changed:
        print(instance.name)
        instance.save()


post_save.connect(validate_times, sender=Masjid)


class MasjidStaff(models.Model):

    name = models.CharField(max_length=128, default="unknown")
    masjid = models.ForeignKey(Masjid, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13)
    action_count = models.PositiveSmallIntegerField(verbose_name="Actions till now", default=1)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {} - {}".format(self.masjid.name, self.name, self.phone)

    @property
    def get_created_on(self):
        return self.created_on.strftime("%d/%m/%Y")
