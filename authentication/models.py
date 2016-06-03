from django.contrib.auth.models import AbstractUser
from django.db import models

from visits.models import PatientCard


class CustomUser(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    medical_right_number = models.CharField(max_length=16, blank=True)

    pesel = models.CharField(max_length=11, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)

    city = models.CharField(max_length=32, blank=True)
    post_code = models.CharField(max_length=32, blank=True)
    address = models.CharField(max_length=64, blank=True)
    telephone = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return self.get_full_name()

    def get_full_address(self):
        return "{post_code} {city}, {address}".format(
            post_code=self.post_code.strip(" "),
            city=self.city.strip(" "),
            address=self.address.strip(" ")
        )
