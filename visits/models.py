from django.conf import settings
from django.db import models


class PatientCard(models.Model):
    registration_date = models.DateTimeField()
    patient = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='my_card')
    main_doctor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='cards')


class Visit(models.Model):
    timestamp = models.DateTimeField()
    reason = models.TextField()
    description = models.TextField()
    card = models.ForeignKey(PatientCard)
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL)
