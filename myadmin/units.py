from django.contrib import messages
from django.shortcuts import render, redirect
from home.forms import *
from home.models import *


def units(request):

    context = {
        'units': Unit.objects.all(),
    }
    return render(request, template_name='admin/pages/units/units.html', context=context)


def addunit(request):
    form = UnitForm()

    if request.method == 'POST':
        form = UnitForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, 'The unit was added successfully')
            unit = form.save()
            return redirect('admin-units-add')
        else:
            messages.error(request, 'An error Occurred while trying to add the unit')

    context = {
        "form": form,
        'update': False
    }
    return render(request, template_name='admin/pages/units/addunit.html', context=context)


def updateunit(request, pk):
    unit = Unit.objects.get(id=pk)
    initial = {
        'title': unit.title,
        'course': unit.course,
    }
    form = UnitForm(initial=initial)

    if request.method == 'POST':
        form = UnitForm(request.POST, request.FILES, instance=unit)
        if form.is_valid():
            form.save()
            messages.success(request, 'The unit was updated successfully')
        else:
            messages.error(request, 'Updating the unit failed')

    context = {
        "form": form,
        'update': True
    }
    return render(request, template_name='admin/pages/units/addunit.html', context=context)


def deleteunit(request, pk):
    course = Unit.objects.get(id=pk)
    if course:
        course.delete()
        messages.success(request, 'The unit was deleted successfully')
    else:
        messages.error(request, 'An error occured while trying to delete the unit')
    context = {}
    return redirect('admin-units')
