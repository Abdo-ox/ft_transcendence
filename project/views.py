from django.shortcuts import render, redirect
from user.models import User 
from .serializer import UserSerializer
from django.http import JsonResponse


def home(request):
    context = {}
    if request.user.is_authenticated:
        users = User.objects.all()
        context['users'] =  users
        return render(request, 'home.html', context)
    else:
        return redirect('login')

def UserData(request):
    users = User.objects.all()
    seriaUsers = UserSerializer(users, many=True)
    return JsonResponse({'users': [seriaUsers.data]})