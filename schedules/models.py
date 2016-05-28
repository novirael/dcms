from django.conf import settings
from django.db import models


class Schedule(models.Model):
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='schedules'
    )


class Term(models.Model):
    date = models.DateField()
    starts = models.TimeField()
    ends = models.TimeField()
    is_free = models.BooleanField()
    schedule = models.ForeignKey(Schedule)
