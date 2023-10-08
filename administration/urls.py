from django.urls import path

from . views import *

urlpatterns = [
    path("", admin_view_redirect, name="redirect"),
    path("dashboard/", admin_view, name="adminview"),
    path("profile/", profile, name="profile"),
    path("settings/", settings, name="settings"),
    path("database/", database_view, name="database"),
    path("documents/", documents, name="documents"),
    path("document/<int:id>", document, name="document"),
]
