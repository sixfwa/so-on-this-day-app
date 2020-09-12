from django.db import models


class Event(models.Model):
    date = models.DateField(verbose_name="date")
    event = models.TextField(verbose_name="event")
    used = models.BooleanField(verbose_name="used")

    def __str__(self):
        return self.event


class DateCollect(models.Model):
    date = models.DateField(verbose_name="date", primary_key=True)
    stored = models.BooleanField(verbose_name="events stored", default=False)
