from django.contrib import admin
from .models import Food, Ordered, Kitchen, Category
# Register your models here.

admin.site.register(Food)
admin.site.register(Ordered)
admin.site.register(Kitchen)
admin.site.register(Category)