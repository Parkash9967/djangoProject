from practice import models
from django.http import HttpResponse
from practice.models import Students
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
@login_required(login_url='login')
def say_hello(request):
    data = Students.objects.all()
    return render(request, 'index.html', {'data': data})


@login_required(login_url='login')
def students(request):
    return render(request, 'students.html')


@login_required(login_url='login')
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
            return redirect('say_hello')

    return render(request, 'index.html')


@login_required(login_url='login')
def update_view(request, id):
    query = models.Students.objects.filter(id=id).all()
    return render(request, 'update.html', {'data': query})


@login_required(login_url='login')
def update_edit(request, id):
    if request.method == "POST":
        query = models.Students.objects.get(id=id)
        query.firstname = request.POST.get("fname")
        query.lastname = request.POST.get("lname")
        query.email = request.POST.get("email")
        query.save()
        return redirect('say_hello')
    return render(request, "update.html")


@login_required(login_url='login')
def delete(request, id):
    Students.objects.filter(id=id).delete()
    return render(request, "index.html")
