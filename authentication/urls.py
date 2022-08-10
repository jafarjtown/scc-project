from django.urls import path
from .views import LogOut, Login, Register
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView,PasswordResetConfirmView, PasswordResetCompleteView

app_name = 'authentication'
urlpatterns = [
    path('login/', Login, name='login'),
    path('register/', Register, name='register'),
    path('logout/', LogOut, name='logout'),
    path('password_reset/', PasswordResetView.as_view(template_name='authentication/forgetten_password.html', success_url='/auth/password_reset_done')),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name='authentication/sent_password.html'), name='password_reset_done'),
    path('password_reset_confirm/', PasswordResetDoneView.as_view(template_name='authentication/sent_password.html'), name='password_reset_done'),
]
