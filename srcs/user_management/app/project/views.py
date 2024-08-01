from django.shortcuts import render, redirect
from user.models import User 
from .serializer import UserSerializer
from django.http import JsonResponse


def home(request):
    context = {}
    if request.user.is_authenticated: #request.user.friend_list.friends.all()
        users = request.user.friends.all()
        print(f"\33[34;1muser: {users}")
        context['users'] =  users
        return render(request, 'home.html', context)
    else:
        return redirect('login')

def UserData(request):
    users = User.objects.all()
    seriaUsers = UserSerializer(users, many=True)
    return JsonResponse({'users': [seriaUsers.data]})