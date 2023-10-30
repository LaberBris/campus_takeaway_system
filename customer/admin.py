
from django.contrib import admin

# Register your models here.

from .models import Canteen, Customer, Orders, UserInfo, Company, Store, Manager, Comment, Dish, Address

admin.site.register(Canteen)
admin.site.register(UserInfo)
admin.site.register(Orders)
admin.site.register(Company)
admin.site.register(Store)
admin.site.register(Manager)
admin.site.register(Customer)
admin.site.register(Comment)
admin.site.register(Dish)
admin.site.register(Address)
