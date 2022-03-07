from django.contrib import messages
from django.shortcuts import render, redirect
from home.forms import *
from home.models import *


def answers(request):

    context = {
        'questions': Answer.objects.all(),
    }
    return render(request, template_name='admin/pages/answers/answers.html', context=context)


def addanswer(request):
    form = AnswerForm()

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            messages.success(request, 'The answer was added successfully')
            answer = form.save()
            return redirect('admin-answers-add')
        else:
            messages.error(request, 'An error Occurred while trying to add the answer')

    context = {
        "form": form,
    }
    return render(request, template_name='admin/pages/answers/addanswer.html', context=context)


def updateanswer(request, pk):
    answer = Answer.objects.get(id=pk)
    initial = {
        'title': answer.title,
        'question': answer.question,
    }
    form = AnswerForm(initial=initial)

    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            form.save()
            messages.success(request, 'The answer was updated successfully')
        else:
            messages.error(request, 'Updating the answer failed')

    context = {
        "form": form,
    }
    return render(request, template_name='admin/pages/answers/addanswer.html', context=context)


def deleteanswer(request, pk):
    answer = Question.objects.get(id=pk)
    if answer:
        answer.delete()
        messages.success(request, 'The answer was deleted successfully')
    else:
        messages.error(request, 'An error occured while trying to delete the answer')
    context = {}
    return redirect('admin-answers')
