from django.contrib.auth.models import AbstractUser
from django.db import models

from visits.models import PatientCard


class CustomUser(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    medical_right_number = models.CharField(max_length=32)
