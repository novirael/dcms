from django.conf.urls import url

from authentication.views import PatientCardDetailView, PatientDetailView, DoctorDetailView

urlpatterns = [
    url(r'^cards/(?P<pk>\d+)/$', PatientCardDetailView.as_view(), name='card_details'),
    url(r'^doctors/(?P<pk>\d+)/$', DoctorDetailView.as_view(), name='doctor_details'),
    url(r'^patients/(?P<pk>\d+)/$', PatientDetailView.as_view(), name='patients_details'),
]
