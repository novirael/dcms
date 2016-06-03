from django.conf.urls import url

from authentication.views import PatientCardDetailView


urlpatterns = [
    url(r'^cards/(?P<pk>\d+)/$', PatientCardDetailView.as_view(), name='card_details'),
]
