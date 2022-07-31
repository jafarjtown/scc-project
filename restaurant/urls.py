
from django.urls import path

from .views import About, Category, CategoryList, Dashboard, Home, OrderFood, OrderHistory, OrderPending, OrderStatus

app_name = 'restaurant'

urlpatterns = [
    path('', Home, name='welcome'),
    path('categories/', Category, name='categories'),
    path('categories/<str:category>/', CategoryList, name='category-list'),
    path('about/', About, name='about'),
    path('dashboard/', Dashboard, name='dashboard'),
    path('order-status/', OrderStatus, name='order-status'),
    path('order-history/', OrderHistory, name='order-history'),
    path('order-pending/', OrderPending, name='order-pending'),
    path('order-food/<int:id>/', OrderFood, name='order-food'),
]
