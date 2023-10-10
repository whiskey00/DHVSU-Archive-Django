from django.urls import path

from . views import *

urlpatterns = [
    path("", library, name="library"),
    path("documents/", documents, name="documents"),
    path("document/<int:id>", document, name="document"),
]
