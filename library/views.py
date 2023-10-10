from django.shortcuts import render, redirect

from . forms import *

def library(request):
    form = DocumentForm()
    context = {}

    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("library")

        print(form.errors)
        return redirect("library")
    
    context["form"] = form.as_p
    return render(request, "library.html", context)

def documents(request):
    documents = Document.objects.all()

    context = {
        "documents" : documents,
    }
    return render(request, "documents.html", context)

def document(request, id):
    document = Document.objects.get(id=id)
    
    context = {
        "document" : document,
    }

    
    return render(request, "document.html", context)