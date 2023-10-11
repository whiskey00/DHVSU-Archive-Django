from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from library.models import *


# Create your views here.
def admin_view_redirect(request):
    return redirect("adminview")

def admin_view(request):
    return render(request, "admin.html", {})

def users(request):
    user = get_user_model()
    _users = user.objects.all()
    context = {
        "users" : _users,
    }

    return render(request, "users.html", context)