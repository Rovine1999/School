from django import forms
from .models import *


class CourseForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-xl shadow-none', 'placeholder': 'Title Eg HTML for beginners'}),
        label='Title')

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control form-control-xl shadow-none', 'rows': 3, 'placeholder': 'Description'}),
        label='Description')

    cost = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control form-control-xl shadow-none', 'placeholder': 'Cost Eg Kes 2, 000 or Free'}),
        label='Cost')

    duration = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control form-control-xl shadow-none', 'placeholder': 'Duration Eg 3 Months'}),
        label='Duration')

    class Meta:
        model = Course
        fields = ['title', 'description', 'cost', 'duration', 'instructor']

        widgets = {
            'instructor': forms.Select(attrs={'class': 'form-control form-control-xl shadow-none'}),
        }


class UnitForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-xl shadow-none', 'placeholder': 'Unit Title'}),
        label='Title')

    class Meta:
        model = Unit
        fields = ['title', 'course']

        widgets = {
            'course': forms.Select(attrs={'class': 'form-control form-control-xl shadow-none'}),
        }


class FileForm(forms.ModelForm):
    file_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-xl shadow-none', 'placeholder': 'File Name'}),
        label='File Name')

    class Meta:
        model = File
        fields = ['unit', 'file_name', 'file']

        widgets = {
            'unit': forms.Select(attrs={'class': 'form-control form-control-xl shadow-none'}),
            'file': forms.FileInput(attrs={'class': 'form-control bg-light border-0'}),
        }


class QuizForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control form-control-xl shadow-none', 'placeholder': 'Quiz Title'}),
        label='Title')

    class Meta:
        model = Quiz
        fields = ['title', 'unit']

        widgets = {
            'unit': forms.Select(attrs={'class': 'form-control form-control-xl shadow-none'}),
        }


class QuestionForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-xl shadow-none', 'placeholder': 'Title'}),
        label='Title')

    class Meta:
        model = Question
        fields = ['quiz', 'title']

        widgets = {
            'quiz': forms.Select(attrs={'class': 'form-control form-control-xl shadow-none'}),
        }


class AnswerForm(forms.ModelForm):
    answer = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control form-control-xl shadow-none', 'rows': 3, 'placeholder': 'Title'}),
        label='Title')

    # correct = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'form-control form-control-xl shadow-none', 'placeholder': 'Title'}),
    #     label='Correct')

    class Meta:
        model = Answer
        fields = ['question', 'answer', 'correct']

        widgets = {
            'question': forms.Select(attrs={'class': 'form-control form-control-xl shadow-none'}),
        }
