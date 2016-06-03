from django.conf.urls import url

from authentication.views import (
    PatientCardDetailView,
    PatientIndexView,
    PatientDetailView,
    DoctorIndexView,
    DoctorDetailView,
)


urlpatterns = [
    url(r'^cards/(?P<pk>\d+)/$', PatientCardDetailView.as_view(), name='card_details'),

    url(r'^doctors/$', DoctorIndexView.as_view(), name='doctor_index'),
    url(r'^doctors/(?P<pk>\d+)/$', DoctorDetailView.as_view(), name='doctor_details'),

    url(r'^patients/$', PatientIndexView.as_view(), name='patient_index'),
    url(r'^patients/(?P<pk>\d+)/$', PatientDetailView.as_view(), name='patient_details'),
]
