from django.contrib import messages
from django.shortcuts import render, redirect
from home.forms import *
from home.models import *
# Create your views here.


def dashboard(request):
    context = {
        'courses': Course.objects.all().count(),
        'units': Unit.objects.all().count(),
        'quizzes': Quiz.objects.all().count(),
    }
    return render(request, template_name='admin/pages/dashboard.html', context=context)


def courses(request):

    context = {
        'courses': Course.objects.all(),
    }
    return render(request, template_name='admin/pages/courses/courses.html', context=context)


def addcourse(request):
    form = CourseForm()

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            messages.success(request, 'The course was added successfully')
            course = form.save()
            return redirect('admin-courses-update', pk=course.id)
        else:
            messages.error(request, 'An error Occurred while trying to add the course')

    context = {
        "form": form,
    }
    return render(request, template_name='admin/pages/courses/addcourse.html', context=context)


def updatecourse(request, pk):
    course = Course.objects.get(id=pk)
    initial = {
        'title': course.title,
        'cost': course.cost,
        'description': course.description,
        'duration': course.duration,
        'instructor': course.instructor
    }
    form = CourseForm(initial=initial)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'The course was updated successfully')
        else:
            messages.error(request, 'Updating the course failed')

    context = {
        "form": form,
    }
    return render(request, template_name='admin/pages/courses/addcourse.html', context=context)


def deletecourse(request, pk):
    course = Course.objects.get(id=pk)
    if course:
        course.delete()
        messages.success(request, 'The course was deleted successfully')
    else:
        messages.error(request, 'An error occured while trying to delete the course')
    context = {}
    return redirect('admin-courses')
