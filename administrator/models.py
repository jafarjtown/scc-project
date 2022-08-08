from django.db import models

# Create your models here.

class RestaurantService(models.Model):
    admin = models.OneToOneField('authentication.User', models.SET_NULL, null=True,  related_name='restaurant')
    kitchens = models.ManyToManyField('kitchen.Kitchen', related_name='restaurant', )
    address = models.TextField()
    name = models.CharField(max_length=25)
    phone_no = models.CharField(max_length=15)
    
    @property
    def customers(self):
        pass
    
    @property
    def orders(self):
        ord = []
        for kt in self.kitchens.all():
            # print(kt.ordered.all())
            ord.extend(kt.ordered.all())
        # print(ord)
        return ord
    
    @property
    def orders_sum(self):
        ord = set()
        obj = {}
        for kt in self.kitchens.all():
            for o in kt.ordered.all():
                if obj.get(str(o.order.ordered_date)) == None:
                    obj[str(o.order.ordered_date)] = {'items': [], 'date': o.order.ordered_date, 'total': 0}
                obj[str(o.order.ordered_date)]['items'].append(o)
                obj[str(o.order.ordered_date)]['total'] += int(o.price)
                # ord.add(o.order)
        print(obj)
        return obj.values()