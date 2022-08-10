
from django.urls import path

from .views import About, AllFoods, Category, CategoryList, Dashboard, Home, OrderFood, OrderHistory, OrderPending, OrderStatus, Profile, UpdateProfile

app_name = 'restaurant'

urlpatterns = [
    path('', Home, name='welcome'),
    path('all_foods', AllFoods, name='all-foods'),
    path('categories/', Category, name='categories'),
    path('categories/<str:category>/', CategoryList, name='category-list'),
    path('about/', About, name='about'),
    path('dashboard/', Dashboard, name='dashboard'),
    path('dashboard/profile/', Profile, name='profile'),
    path('dashboard/profile/update/', UpdateProfile, name='update_profile'),
    path('dashboard/order-status/', OrderStatus, name='order-status'),
    path('dashboard/order-history/', OrderHistory, name='order-history'),
    path('dashboard/order-pending/', OrderPending, name='order-pending'),
    path('dashboard/order-food/<int:id>/', OrderFood, name='order-food'),
]
