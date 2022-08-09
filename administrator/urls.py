
from django.urls import path
from . import views

app_name = 'administrator'
urlpatterns = [
    path('', views.Dashboard, name='dashboard'),
    path('orders/', views.Orders, name='orders'),
    path('profile/', views.Profile, name='profile'),
    path('customers/', views.StudentCustomers, name='student-customers'),
    path('orders-summary/', views.OrderSummary, name='orders-summary'),
]
