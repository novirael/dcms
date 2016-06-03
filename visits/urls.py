from django.conf.urls import url

from visits.views import VisitIndexView, VisitDetailView


urlpatterns = [
    url(r'^$', VisitIndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', VisitDetailView.as_view(), name='details'),
]
