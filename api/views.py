from django.shortcuts import render
from django.http import HttpResponse
from django.middleware.csrf import get_token

def serve_request(request):
    csrftoken = get_token(request)
    html_content = render(request, 'index.html')
    response = HttpResponse(html_content)
    response['X-CSRFToken'] = csrftoken
    return response

def recieveData(request):
    print(request.body)
    hello = render(request , 'index.html')
    return HttpResponse(request.body)