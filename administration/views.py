from django.shortcuts import render, redirect

from library.models import *

# Create your views here.
def admin_view_redirect(request):
    return redirect("adminview")

def admin_view(request):
    return render(request, "admin.html", {})

def users(request):
    return render(request, "users.html")