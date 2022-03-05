from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField( max_length=200)
    description = models.TextField(max_length=5000)
    cost = models.CharField(max_length=50)
    duration = models.CharField(max_length=200)
    instructor = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)


class Unit(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=3000)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)


class File(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=500)
    file = models.FileField(upload_to='files/')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)


class Quiz(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    title = models.TextField(max_length=3000)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True)
    answer = models.TextField(max_length=1000)
    correct = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
