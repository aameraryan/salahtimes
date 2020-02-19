import datetime
import time

from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse_lazy

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
        instance.save()


post_save.connect(validate_times, sender=Masjid)


# if instance.zuhar < datetime.time(12, 0, 0):
#     instance.zuhar = (datetime.datetime.combine(datetime.date(1, 1, 1), instance.zuhar) +
#                       datetime.timedelta(hours=12)).time()
# if instance.asar < datetime.time(12, 0, 0):
#     instance.asar = (datetime.datetime.combine(datetime.date(1, 1, 1), instance.asar) +
#                      datetime.timedelta(hours=12)).time()
# if instance.maghrib < datetime.time(12, 0, 0):
#     instance.maghrib = (datetime.datetime.combine(datetime.date(1, 1, 1), instance.maghrib) +
#                         datetime.timedelta(hours=12)).time()
# if instance.isha < datetime.time(12, 0, 0):
#     instance.isha = (datetime.datetime.combine(datetime.date(1, 1, 1), instance.isha) +
#                      datetime.timedelta(hours=12)).time()
# if instance.juma < datetime.time(12, 0, 0):
#     instance.juma = (datetime.datetime.combine(datetime.date(1, 1, 1), instance.juma) +
#                      datetime.timedelta(hours=12)).time()

