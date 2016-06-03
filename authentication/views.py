from django.views.generic import DetailView

from visits.models import PatientCard


class PatientCardDetailView(DetailView):
    template_name = 'authentication/card_details.html'
    model = PatientCard
    context_object_name = 'card'
