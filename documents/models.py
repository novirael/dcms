from django.conf import settings
from django.db import models


class Document(models.Model):
    created_date = models.DateTimeField()
    description = models.TextField()
    number = models.CharField(max_length=32)
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='doctor_%(class)s')
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='patient_%(class)s')
    visit = models.ForeignKey('visits.Visit', related_name='%(class)s')

    class Meta:
        abstract = True


class Referral(Document):
    pass


class Prescription(Document):
    pass


class Receipt(Document):
    is_invoice = models.BooleanField()
    total_value = models.DecimalField(max_digits=8, decimal_places=2)
