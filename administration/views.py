from django.shortcuts import render, redirect

from library.models import *

# Create your views here.
def admin_view_redirect(request):
    return redirect("adminview")

def admin_view(request):
    return render(request, "admin.html", {})

def profile(request):
    return render(request, "profile.html", {})

def settings(request):
    return render(request, "settings.html")

def database_view(request):
    return render(request, "database.html")