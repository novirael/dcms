from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView

from authentication.models import CustomUser
from visits.models import PatientCard


class UserIndexView(ListView):
    template_name = 'authentication/index.html'
    model = CustomUser
    context_object_name = 'people'
    paginate_by = 20
    is_doctor = None

    def get_context_data(self, **kwargs):
        context = super(UserIndexView, self).get_context_data(**kwargs)
        context['is_doctor'] = self.is_doctor
        return context


class PatientCardDetailView(DetailView):
    template_name = 'authentication/card_details.html'
    model = PatientCard
    context_object_name = 'card'


class DoctorIndexView(UserIndexView):
    is_doctor = True
    queryset = CustomUser.objects.filter(
        groups__name__in=["Doctor"]
    )


class DoctorDetailView(DetailView):
    template_name = 'authentication/doctor_details.html'
    model = CustomUser
    context_object_name = 'doctor'
    queryset = CustomUser.objects.filter(
        groups__name__in=["Doctor"]
    )


class PatientIndexView(UserIndexView):
    is_doctor = False
    queryset = CustomUser.objects.filter(
        groups__name__in=["Patient"]
    )


class PatientDetailView(DetailView):
    template_name = 'authentication/patient_details.html'
    model = CustomUser
    context_object_name = 'patient'
    queryset = CustomUser.objects.filter(
        groups__name__in=["Patient"]
    )
