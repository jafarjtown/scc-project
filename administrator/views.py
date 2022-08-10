from django.shortcuts import redirect, render

from administrator.forms import BlogForm
from administrator.models import Blog
from decorators import administrator_only

# Create your views here.


@administrator_only
def Dashboard(request):
    return render(request, 'administrator/dashboard.html')

@administrator_only
def Profile(request):
    return render(request, 'administrator/profile.html')

@administrator_only
def Blogs(request):
    blogs = request.user.posts.all()
    return render(request, 'administrator/posts.html', {'posts': blogs})
@administrator_only
def NewBlog(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
    return render(request, 'administrator/new-post.html', {'form': form})

@administrator_only
def UpdateBlog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    form = BlogForm(instance=blog)
    if request.method == 'DELET':
        blog.delete()
        return redirect('administrator:posts')
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
    return render(request, 'administrator/new-post.html', {'form': form})

@administrator_only
def NotAvailable(request):
    foods = request.user.restaurant.not_available_foods
    return render(request, 'administrator/not-available.html', {'foods': foods})
@administrator_only
def Orders(request):
    user = request.user
    orders = []
    restaurant = user.restaurant
    orders.extend(restaurant.orders)
    return render(request, 'administrator/orders.html', {'orders': orders})

@administrator_only
def StudentCustomers(request):
    user = request.user
    customers = set()
    restaurant = user.restaurant
    for ord in restaurant.orders:
        print(ord)
        customers.add(ord.customer)
    return render(request, 'administrator/customers.html', {'customers':customers})

@administrator_only
def OrderSummary(request):
    user = request.user
    orders = []
    restaurant = user.restaurant
    print(restaurant)
    orders.extend(restaurant.orders_sum)
    print(orders)
    return render(request, 'administrator/order-summary.html', {'orders': orders})


@administrator_only
def Foods(request):
    user = request.user
    foods = user.restaurant.foods
    return render(request, 'administrator/foods.html', {'foods': foods})

@administrator_only
def Kitchens(request):
    user = request.user
    kitchens = user.restaurant.kitchens.all()
    return render(request, 'administrator/kitchens.html', {'kitchens':kitchens})