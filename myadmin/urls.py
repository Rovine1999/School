from django.urls import path

from . import views
from . import units
from . import quizzes
from . import questions
from . import answers

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('courses/', views.courses, name='admin-courses'),
    path('courses/add/', views.addcourse, name='admin-courses-add'),
    path('courses/update/<str:pk>/', views.updatecourse, name='admin-courses-update'),
    path('courses/delete/<str:pk>/', views.deletecourse, name='admin-courses-delete'),

    path('units/', units.units, name='admin-units'),
    path('units/add/', units.addunit, name='admin-units-add'),
    path('units/update/<str:pk>/', units.updateunit, name='admin-units-update'),
    path('units/delete/<str:pk>/', units.deleteunit, name='admin-units-delete'),

    path('quizzes/', quizzes.quizzes, name='admin-quizzes'),
    path('quizzes/add/', quizzes.addquizzes, name='admin-quizzes-add'),
    path('quizzes/update/<str:pk>/', quizzes.updatequizzes, name='admin-quizzes-update'),
    path('quizzes/delete/<str:pk>/', quizzes.deletequizzes, name='admin-quizzes-delete'),

    path('questions/', questions.questions, name='admin-questions'),
    path('questions/add/', questions.addquestion, name='admin-questions-add'),
    path('questions/update/<str:pk>/', questions.updatequestion, name='admin-questions-update'),
    path('questions/delete/<str:pk>/', questions.deletequestion, name='admin-questions-delete'),

    path('answers/', answers.answers, name='admin-answers'),
    path('answers/add/', answers.addanswer, name='admin-answers-add'),
    path('answers/update/<str:pk>/', answers.updateanswer, name='admin-answers-update'),
    path('answers/delete/<str:pk>/', answers.deleteanswer, name='admin-answers-delete'),

]
