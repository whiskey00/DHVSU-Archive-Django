from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from . forms import *

def authentication(request):
    context = {}

    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST" and request.POST.get("login-button"):
        
        username = request.POST.get("username")
        password = request.POST.get("password")
    
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            print("Logged in!")
            return redirect("home")

        
    form = RegisterForm(request.POST or None)

    if request.method == "POST" and request.POST.get("register-button"):
        if(form.is_valid()):
            form.save()
            form = RegisterForm()
            return redirect("home")

    context['form'] = form

    return render(request, "authentication.html", context)

def logout_view(request):
    logout(request)
    return redirect("authentication:authentication")