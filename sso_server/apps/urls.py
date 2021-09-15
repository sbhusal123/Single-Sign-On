from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="home")
]
