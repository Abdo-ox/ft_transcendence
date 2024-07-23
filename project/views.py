from django.shortcuts import render, redirect
from user.models import User 
def home(request):
    context = {}
    if request.user.is_authenticated:
        users = User.objects.all()
        context['users'] =  users
        return render(request, 'home.html', context)
    else:
        return redirect('login')