from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView, TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^admin/', admin.site.urls),
    url(r'^visits/', include('visits.urls', namespace='visits')),
]
