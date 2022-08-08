from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import F
# from SPRINT_PROJECT.kitchen.models import Food
from kitchen.models import Category as Cat, Food, Order, Ordered
# Create your views here.


def Home(request):
    return render(request, 'restaurant/index.html')

def Category(request):
    categories = Cat.objects.all()
    context = {'categories': categories}
    return render(request, 'restaurant/categories.html', context)

def CategoryList(request, category):
    try:
        foods = Cat.objects.get(name = category).foods.all()
        context = { "category": category, 'foods': foods}
        return render(request, 'restaurant/cat-list.html', context)
    except:
        return redirect('restaurant:categories')

def About(request):
    return render(request, 'restaurant/about.html')
def OrderFood(request, id):
    if request.method == 'POST':
        import datetime
        food = Food.objects.get(id=id)
        today = datetime.date.today()
        order_list = Order.objects.get_or_create(ordered_date = today, customer=request.user)
        ordered = Ordered.objects.create(name=food.name,image=food.image.url, price=food.price, quantity=request.POST.get('quantity'),category=food.category,delivery_point=request.POST.get('delivery_point'),phone_no=request.POST.get('phone_no'))
        order_list[0].items.add(ordered)
        order_list[0].save()
        food.quantity = F('quantity') - int(request.POST.get('quantity'))
        food.save()
        if food.kitchen_offered is not None:
            ordered.kitchen=food.kitchen_offered
            ordered.save()
        return redirect('restaurant:categories')
@login_required
def Dashboard(request):
    return render(request, 'restaurant/dashboard.html')
@login_required
def OrderStatus(request):
    return render(request, 'restaurant/order-status.html')
@login_required
def OrderHistory(request):
    context = {}
    all_orders = request.user.order_set.all()
    context['orders'] = all_orders
    return render(request, 'restaurant/order-history.html', context)
@login_required
def OrderPending(request):
    return render(request, 'restaurant/order-pending.html')