from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .email import send_welcome_email
# Create your views here.


# @login_required(login_url='login')
def home(request):
    if request.method == 'POST':
            email = request.POST.get('email')
            recipient = NewsLetterRecipients(email =email)
            recipient.save()
            send_welcome_email(email)
            HttpResponseRedirect('home')

    context = {
        'featured_courses': Course.objects.all(),
        'recent_courses': Course.objects.all(),
        'popular_courses': Course.objects.all(),
        'upcoming_courses': Course.objects.all(),

    }
    return render(request, template_name='home/pages/index.html', context=context)


def courses(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, template_name='home/pages/courses.html', context=context)


def contactus(request):
    return render(request, template_name='home/pages/contact.html')


def aboutus(request):
    return render(request, template_name='home/pages/about.html')


def faq(request):
    return render(request, template_name='home/pages/faq.html')


def notfound(request, exception):
    return render(request, template_name='errors/pages/404.html')


def internalservererror(request):
    return render(request, template_name='errors/pages/500.html')


def unauthorizedaccess(request, exception):
    return render(request, template_name='errors/pages/403.html')
