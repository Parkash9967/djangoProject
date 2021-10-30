from django.shortcuts import render
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from practice import models
from django.contrib import messages
from practice.forms import StudentForm
from django.http import HttpResponse
from practice.models import Students


# Create your views here.
def say_hello(request):
    # context = {}
    # context["data"] = Students.objects.all()
    data = Students.objects.all()
    return render(request, 'index.html', {'data': data})


def students(request):
    return render(request, 'students.html')


# def addStudents(request):
#     form = StudentForm
#
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context = {'form': form}
#     return render(request, 'index.html', context)

def addStudents(request):
    if request.method == "POST":
        instance = models.Students()
        email = request.POST.get("email")
        user = models.Students.objects.filter(email=email).first()
        if user:
            text = """<h1>hello</h1>"""
            return HttpResponse(text)
        else:
            instance.firstname = request.POST.get("fname")
            instance.lastname = request.POST.get("lname")
            instance.email = request.POST.get("email")
            instance.save()
            return render(request, 'index.html')

    return render(request, 'index.html')


def update_view(request, id):
    query = models.Students.objects.filter(id=id).all()
    return render(request, 'update.html', {'data': query})


def update_edit(request, id):
    if request.method == "POST":
        query = models.Students.objects.get(id=id)
        query.firstname = request.POST.get("fname")
        query.lastname = request.POST.get("lname")
        query.email = request.POST.get("email")
        query.save()
        return render(request, "index.html")
    return render(request, "update.html")


def delete(request, id):
    Students.objects.filter(id=id).delete()
    return render(request, "index.html")
