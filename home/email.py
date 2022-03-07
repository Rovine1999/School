from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(email):
    # Creating message subject and sender
    subject = 'Welcome to the CourseSchool'
    sender = 'rovinewanjala99@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/newsemail.txt',{"email": email})
    html_content = render_to_string('email/newsemail.html',{"email": email})

    msg = EmailMultiAlternatives(subject,text_content,sender,[email])
    msg.attach_alternative(html_content,'text/html')
    msg.send()