from django.shortcuts import render

# Create your views here.


def Dashboard(request):
    return render(request, 'administrator/dashboard.html')

def Profile(request):
    return render(request, 'administrator/profile.html')


def Orders(request):
    user = request.user
    orders = []
    restaurant = user.restaurant
    orders.extend(restaurant.orders)
    return render(request, 'administrator/orders.html', {'orders': orders})


def StudentCustomers(request):
    user = request.user
    customers = set()
    restaurant = user.restaurant
    for ord in restaurant.orders:
        print(ord)
        customers.add(ord.customer)
    return render(request, 'administrator/customers.html', {'customers':customers})


def OrderSummary(request):
    user = request.user
    orders = []
    restaurant = user.restaurant
    print(restaurant)
    orders.extend(restaurant.orders_sum)
    print(orders)
    return render(request, 'administrator/order-summary.html', {'orders': orders})
