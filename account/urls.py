from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.account_login, name='login'),
    path('logout/', views.account_logout, name='logout'),
    path('signup/', views.login, name='signup')
]
