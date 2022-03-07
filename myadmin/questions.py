from django.contrib import messages
from django.shortcuts import render, redirect
from home.forms import *
from home.models import *


def questions(request):

    context = {
        'questions': Question.objects.all(),
    }
    return render(request, template_name='admin/pages/questions/questions.html', context=context)


def addquestion(request):
    form = QuestionForm()

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            messages.success(request, 'The question was added successfully')
            question = form.save()
            return redirect('admin-questions-add')
        else:
            messages.error(request, 'An error Occurred while trying to add the question')

    context = {
        "form": form,
    }
    return render(request, template_name='admin/pages/questions/addquestion.html', context=context)


def updatequestion(request, pk):
    question = Question.objects.get(id=pk)
    initial = {
        'title': question.title,
        'course': question.course,
    }
    form = QuestionForm(initial=initial)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            messages.success(request, 'The question was updated successfully')
        else:
            messages.error(request, 'Updating the question failed')

    context = {
        "form": form,
    }
    return render(request, template_name='admin/pages/questions/addquestion.html', context=context)


def deletequestion(request, pk):
    question = Question.objects.get(id=pk)
    if question:
        question.delete()
        messages.success(request, 'The question was deleted successfully')
    else:
        messages.error(request, 'An error occured while trying to delete the question')
    context = {}
    return redirect('admin-questions')
