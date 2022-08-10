
from django.urls import path
from . import views

app_name = 'administrator'
urlpatterns = [
    path('', views.Dashboard, name='dashboard'),
    path('orders/', views.Orders, name='orders'),
    path('profile/', views.Profile, name='profile'),
    path('foods/', views.Foods, name='foods'),
    path('kitchens/', views.Kitchens, name='kitchens'),
    path('posts/', views.Blogs, name='posts'),
    path('config-post/', views.NewBlog, name='config-post'),
    path('config-post/<int:blog_id>/', views.UpdateBlog, name='update-post'),
    path('customers/', views.StudentCustomers, name='student-customers'),
    path('orders-summary/', views.OrderSummary, name='orders-summary'),
    path('not-available/', views.NotAvailable, name='not-available'),
]
