from django.shortcuts import render, redirect

from . forms import *

def library(request):
    form = DocumentForm()
    context = {}

    if request.method == "POST":
        form = DocumentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("library")

        return redirect("library")
    
    context["form"] = form.as_p
    print(form)
    return render(request, "library.html", context)