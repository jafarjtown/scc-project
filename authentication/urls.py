from django.urls import path
from .views import LogOut, Login, Register

app_name = 'authentication'
urlpatterns = [
    path('login/', Login, name='login'),
    path('register/', Register, name='register'),
    path('logout/', LogOut, name='logout'),
]
