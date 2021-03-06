from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('authentication.urls', namespace='users')),
    url(r'^visits/', include('visits.urls', namespace='visits')),
]
