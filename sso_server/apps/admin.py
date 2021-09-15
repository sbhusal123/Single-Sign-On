from django.contrib import admin

from simple_sso.sso_server.models import Token

admin.site.register(Token)
