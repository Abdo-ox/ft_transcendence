from django.urls import path
from .views import Login, register

urlpatterns = [
    path('register/', register, name='register'),
    path('login/',Login, name='login'),
]