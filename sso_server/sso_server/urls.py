from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url


from .sso_server import Server

sso_server = Server()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.urls')),

    # for sso login form, Template: /registraton/login.html
    path('', include('django.contrib.auth.urls')),

    # SSO_SERVER = xxx.com/server. This is where SSO authentication gets handled at server side
    url(r'^server/', include(sso_server.get_urls()))
]
