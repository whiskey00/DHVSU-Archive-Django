from django.shortcuts import render, redirect

# Create your views here.
def admin_view_redirect(request):
    return redirect("adminview")

def admin_view(request):
    return render(request, "admin.html", {})

def profile(request):
    return render(request, "profile.html", {})