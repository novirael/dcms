from django.views.generic import ListView, DetailView

from visits.models import Visit
from datetime import datetime, timedelta


class VisitIndexView(ListView):
    template_name = 'visits/index.html'
    model = Visit
    context_object_name = 'past_visits'
    today = datetime.now().date()
    tomorrow = today + timedelta(days=1)
    related = ('doctor', 'card', 'card__patient')
    queryset = Visit.objects.filter(timestamp__lt=today).select_related(*related)
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(VisitIndexView, self).get_context_data(**kwargs)
        context['todays_visits'] = Visit.objects.filter(
            timestamp__range=(self.today, self.tomorrow)
        ).select_related(*self.related)
        context['future_visits'] = Visit.objects.filter(
            timestamp__gt=self.tomorrow
        ).select_related(*self.related)
        return context


class VisitDetailView(DetailView):
    template_name = 'visits/details.html'
    model = Visit
    context_object_name = 'visit'
