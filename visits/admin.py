from django.contrib import admin

from visits.models import PatientCard, Visit


class PatientCardAdmin(admin.ModelAdmin):
    list_display = ("registration_date", "patient", "main_doctor")


class VisitAdmin(admin.ModelAdmin):
    list_display = ("timestamp", "get_patient", "doctor")
    list_filter = ("timestamp", "card__patient", "doctor")

    def get_patient(self, obj):
        return obj.card.patient

    get_patient.admin_order_field = 'card__patient'
    get_patient.short_description = 'Patient'


admin.site.register(PatientCard, PatientCardAdmin)
admin.site.register(Visit, VisitAdmin)
