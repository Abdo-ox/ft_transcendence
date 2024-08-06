from django.contrib import admin
from django.urls import path, include
from .views import home, UserData, getCsrfToken

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('api/csrf_token/', getCsrfToken),
    path('api/', include('user.urls')),
]
