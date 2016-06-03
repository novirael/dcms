from django.conf import settings
from django.db import models


class PatientCard(models.Model):
    registration_date = models.DateTimeField()
    insurance = models.TextField(max_length=16, blank=True)
    patient = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='my_card')
    main_doctor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='cards')


class Visit(models.Model):
    timestamp = models.DateTimeField()
    reason = models.TextField(blank=True)
    description = models.TextField(blank=True)
    card = models.ForeignKey(PatientCard)
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ('-timestamp',)
