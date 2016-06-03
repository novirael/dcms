from django.views.generic import DetailView

from authentication.models import CustomUser
from visits.models import PatientCard


class PatientCardDetailView(DetailView):
    template_name = 'authentication/card_details.html'
    model = PatientCard
    context_object_name = 'card'


class DoctorDetailView(DetailView):
    template_name = 'authentication/doctor_details.html'
    model = CustomUser
    context_object_name = 'doctor'
    queryset = CustomUser.objects.filter(
        groups__name__in=["Doctor"]
    )


class PatientDetailView(DetailView):
    template_name = 'authentication/patient_details.html'
    model = CustomUser
    context_object_name = 'patient'
    queryset = CustomUser.objects.filter(
        groups__name__in=["Patient"]
    )
