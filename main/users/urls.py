from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.render, name='register'),
    path('login/', views.login_user, name='login'),
]
