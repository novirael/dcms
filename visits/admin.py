from django.contrib import admin

from visits.models import PatientCard, Visit


admin.site.register(PatientCard)
admin.site.register(Visit)
