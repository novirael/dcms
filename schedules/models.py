from django.conf import settings
from django.db import models


class Schedule(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='schedules'
    )


class Term(models.Model):
    date = models.DateField()
    starts = models.TimeField()
    ends = models.TimeField()
    is_free = models.BooleanField(default=False)
    schedule = models.ForeignKey(Schedule)

    def __str__(self):
        return "{}, {} - {}".format(
            self.date, self.starts, self.ends
        )

    class Meta:
        ordering = ("-date", "-starts")
