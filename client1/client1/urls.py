from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from django.views.generic import TemplateView

from django.conf import settings
from .sso_client import Client

sso_client = Client(settings.SSO_SERVER, settings.SSO_PUBLIC_KEY, settings.SSO_PRIVATE_KEY)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),

    path('', TemplateView.as_view(template_name="index.html"), name="home"),

    # Client SSO
    url(r'^client/', include(sso_client.get_urls()))
]
