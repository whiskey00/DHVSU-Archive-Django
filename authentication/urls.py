from django.urls import path

from . views import *

app_name = 'authentication'

urlpatterns = [
    path("", authentication, name="authentication"),
    path("logout", logout_view, name="logout")
]
