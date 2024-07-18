from django.shortcuts import render, redirect
from user.forms import RegisterationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
import urllib.parse
import requests
from user.models import User

def Login(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            context['form'] = form
    return render(request, 'login.html', context)

def Register(request):
    context = {}
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context['form'] = form
    return render(request, 'register.html', context)

def Oauth_42(request):
    conf  = settings.OAUTH_CONFIG['42']
    params = {
        'client_id' : conf['client_id'],
        'redirect_uri' : conf['redirect_uri'],
        'response_type' : 'code'
    }
    url = f"{conf['base_url']}?{urllib.parse.urlencode(params)}"
    print("\33[31;1m", url)
    return redirect(url)

def Oauth_42_callback(request):
    conf  = settings.OAUTH_CONFIG['42']
    code = request.GET.get('code')
    params = {
        'client_id': conf['client_id'],
        'client_secret': conf['client_secret'],
        'grant_type': 'authorization_code',
        'redirect_uri': conf['redirect_uri'],
        'code': code
    }
    response = requests.post(conf['token_url'], data=params)
    access_token  = response.json()['access_token']
    response = requests.get(conf['info_url'], params={'access_token' : access_token})
    data = response.json()
    info_usr = {
        'email' : data['email'],
        'first_name' : data['first_name'],
        'last_name' : data['last_name'],
        'profile_image' : data['image']['versions']['medium'],
    }
    User.objects.create_user(data['login'], None, **info_usr)
    return redirect('login')

def Logout(request):
    logout(request)
    return redirect('login')