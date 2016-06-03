from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView


urlpatterns = [
    url(r'^$', RedirectView.as_view(url='visits/')),
    url(r'^admin/', admin.site.urls),
    url(r'^visits/', include('visits.urls', namespace='visits')),
]
