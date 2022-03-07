from django.contrib import messages
from django.shortcuts import render, redirect
from home.forms import *
from home.models import *


def quizzes(request):

    context = {
        'quizzes': Quiz.objects.all(),
    }
    return render(request, template_name='admin/pages/quizzes/quizzes.html', context=context)


def addquizzes(request):
    form = QuizForm()

    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            messages.success(request, 'The quiz was added successfully')
            quiz = form.save()
            return redirect('admin-quizzes-add')
        else:
            messages.error(request, 'An error Occurred while trying to add the quiz')

    context = {
        "form": form,
    }
    return render(request, template_name='admin/pages/quizzes/addquiz.html', context=context)


def updatequizzes(request, pk):
    quiz = Quiz.objects.get(id=pk)
    initial = {
        'title': quiz.title,
        'unit': quiz.unit,
    }
    form = QuizForm(initial=initial)

    if request.method == 'POST':
        form = QuizForm(request.POST, instance=quiz)
        if form.is_valid():
            form.save()
            messages.success(request, 'The quiz was updated successfully')
        else:
            messages.error(request, 'Updating the quiz failed')

    context = {
        "form": form,
    }
    return render(request, template_name='admin/pages/quizzes/addquiz.html', context=context)


def deletequizzes(request, pk):
    quiz = Quiz.objects.get(id=pk)
    if quiz:
        quiz.delete()
        messages.success(request, 'The quiz was deleted successfully')
    else:
        messages.error(request, 'An error occured while trying to delete the quiz')
    context = {}
    return redirect('admin-quizzes')
