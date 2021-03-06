from email.mime import image
from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Course(models.Model):
    title = models.CharField( max_length=200)
    description = models.TextField(max_length=5000)
    cost = models.CharField(max_length=50)
    duration = models.CharField(max_length=200)
    instructor = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image')

    def __str__(self):
        return self.title


class Unit(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=3000)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image')

    def __str__(self):
        return self.title


class File(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=500)
    file = CloudinaryField('image')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.unit

class Quiz(models.Model):
    title = models.TextField(max_length=300, blank=True, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    title = models.TextField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quiz

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True)
    answer = models.TextField(max_length=1000)
    correct = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

class NewsLetterRecipients(models.Model):
    email = models.EmailField()
