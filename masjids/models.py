import datetime
import time

from django.db import models
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

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     if self.id:
    #         print("has id")
    #         if self.fajar > datetime.time(12, 0, 0):
    #             self.fajar = (datetime.datetime.combine(datetime.date(1, 1, 1), self.fajar) -
    #                           datetime.timedelta(hours=12)).time()
    #         if self.zuhar < datetime.time(12, 0, 0):
    #             self.zuhar = (datetime.datetime.combine(datetime.date(1, 1, 1), self.zuhar) +
    #                           datetime.timedelta(hours=12)).time()
    #         if self.asar < datetime.time(12, 0, 0):
    #             self.asar = (datetime.datetime.combine(datetime.date(1, 1, 1), self.asar) +
    #                           datetime.timedelta(hours=12)).time()
    #         if self.maghrib < datetime.time(12, 0, 0):
    #             self.maghrib = (datetime.datetime.combine(datetime.date(1, 1, 1), self.maghrib) +
    #                           datetime.timedelta(hours=12)).time()
    #         if self.isha < datetime.time(12, 0, 0):
    #             self.isha = (datetime.datetime.combine(datetime.date(1, 1, 1), self.isha) +
    #                           datetime.timedelta(hours=12)).time()
    #         if self.juma < datetime.time(12, 0, 0):
    #             self.juma = (datetime.datetime.combine(datetime.date(1, 1, 1), self.juma) +
    #                           datetime.timedelta(hours=12)).time()
    #         super().save()

    def get_address_display(self):
        return "{}".format(self.address)

    class Meta:
        verbose_name = "Masjid"
        verbose_name_plural = "Masajid"

    @property
    def get_update_url(self):
        return reverse_lazy("masjids:update", kwargs={"id": self.id})
