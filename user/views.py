from django.shortcuts import render
from user.forms import RegisterationForm

def Login(request):
    return render(request, 'login.html')

def register(request):
    context = {}
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request, 'home')
        else:
            context['form'] = form
    print(context)
    return render(request, 'register.html', context)