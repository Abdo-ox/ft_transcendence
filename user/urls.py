from django.urls import path
from .views import Login, Register, Logout, Oauth_42, Oauth_42_callback

urlpatterns = [
    path('register/', Register, name='register'),
    path('login/',Login, name='login'),
    path('logout/',Logout, name='logout'),
    path('42/',Oauth_42, name='42'),
    path('42/callback/', Oauth_42_callback, name='42'),
]