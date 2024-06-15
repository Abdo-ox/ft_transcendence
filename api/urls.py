from django.urls import path
from . import views

urlpatterns  = [
    path('', views.serve_request),
    path('submit', views.recieveData),
]