from django.urls import path
from .views import cmp_manage, cmp_store, cmp_dish, cmp_order

urlpatterns = [
    path('', cmp_manage, name='cmp_manage'),
    path('store/', cmp_store, name='cmp_store'),
    path('dish/', cmp_dish, name='cmp_dish'),
    path('order/', cmp_order, name='cmp_order'),
]
