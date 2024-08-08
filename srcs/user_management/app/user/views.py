from django.shortcuts import render, redirect
from user.forms import RegisterationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from django.conf import settings
import urllib.parse
import requests
import json
from user.models import User
from django.http import JsonResponse
from project.settings import C as c

@api_view(['POST'])
def Login(request):
    data = json.loads(request.body)
    form = LoginForm(data)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/home.html')
    errors = form.errors.as_json()
    return JsonResponse(json.loads(errors))

@api_view(['POST'])
def Register(request):
    form = RegisterationForm(request.data)
    if form.is_valid():
        password = form.cleaned_data['password1']
        user = form.save()
        print("\33[32;1m", user.username, "\33[0m")
        print("\33[32;1m", password, "\33[0m")
        user.set_password(password)
        user.save()
        return redirect('/login.html')
    errors = form.errors.as_json()
    return JsonResponse(json.loads(errors))

def printJsonData(data):
    for key, value in data.items():
        if isinstance(value, dict):
            print(f"{c.g} {key}:")
            print("=============================================================================>")
            printJsonData(value)
        else:
            print(f"{c.b}{key}: {value}")

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
    print(f"\33[34;1m{params}")
    response = requests.post(conf['token_url'], data=params)
    if response.status_code == 200:
        access_token  = response.json()['access_token']
        response = requests.get(conf['info_url'], params={'access_token' : access_token})
        data = response.json()
        printJsonData(data)
        user = authenticate(username=data['login'])
        if user:
            login(request, user)
            return redirect('home')
        info_usr = {
            'email' : data['email'],
            'first_name' : data['first_name'],
            'last_name' : data['last_name'],
            'profile_image' : data['image']['versions']['medium'],
        }
        User.objects.create_user(data['login'], None, **info_usr)
        return redirect('login')
    print(f"here{c}")
    print(f"{c.r}statusCodeOf the token response:{response.status_code}{c.d}")
    

def Logout(request):
    logout(request)
    return redirect('login')