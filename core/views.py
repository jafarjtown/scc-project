from django.utils import timezone
from multiprocessing import context
import random
import string
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
from . import models


def products(request):
    context = {
        'items': models.Item.objects.all()
    }
    return render(request, "products.html", context)


def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid

def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))

def ItemView(request):
    items = models.Item.objects.all()
    context = {
        "items":items
    }
    return render(request, 'core/index.html', context=context)


# def ItemDetailView(request, slug):
#     items = models.Item.objects.get(slug=slug)
#     context = {
#         "item":items
#     }
#     return render(request, 'core/detail.html', context=context)

def ItemDetailView(request, slug):
    items = models.Item.objects.get(slug=slug)
    context = {
        "item":items
    }
    return render(request, 'core/detail.html', context=context)


@login_required
def add_to_cart(request, slug):
    print(request.user)
    item = get_object_or_404(models.Item, slug=slug)
    order_item, created = models.OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    # print(slug)
    order_qs = models.Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect('core:item-view', slug=slug)

        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect('core:item-view', slug=slug)
    else:
        ordered_date = timezone.now()
        order = models.Order.objects.create(
            user=request.user, ordered_date=ordered_date, ref_code=create_ref_code())
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect('core:item-view', slug=slug)

class order_summary(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = models.Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            print(order.items)
            return render(self.request, 'core/order_summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")

# @login_required
# def order_summary(self):
#     try:
#         order = Order.objects.get(user=self.request.user, ordered=False)
#         context = {
#             'object': order
#         }
#         return render(self.request, 'order_summary.html', context)
#     except ObjectDoesNotExist:
#         messages.warning(self.request, "You do not have an active order")
#         return redirect("core:item-view")

@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(models.Item, slug=slug)
    order_qs = models.Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = models.OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("core:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("core:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:product", slug=slug)



@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(models.Item, slug=slug)
    order_qs = models.Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = models.OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "This item quantity was updated.")
            return redirect("core:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("core:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:product", slug=slug)
