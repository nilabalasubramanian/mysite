from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from HelloWorld.models import Employee
from HelloWorld.forms import Employee_form


def index(request):
    return render(request, 'home.html')


def create_view(request):
    form = Employee_form()
    if request.method == "POST":
        form = Employee_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('./display')
    return render(request, 'insert.html', context={'form': form})


def retrieve_view(request):
    employee = Employee.objects.all()
    return render(request, "index.html", context={"employee": employee})


def update_view(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == "POST":
        form = Employee_form(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../display')
    return render(request, "update.html", context={"employee": employee})


def delete_view(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return HttpResponseRedirect('../display')
