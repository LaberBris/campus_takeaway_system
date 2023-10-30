from django.urls import path

from dish.views import dish, comment, cus_comment
from .views import login, signup, logout, address, index

urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
    path('address/', address, name='address'),
    path('index/', index, name='index'),
    path('dish/', dish, name='cus_dish'),
    path('comment/', comment, name='cus_comment'),
    path('write_comment/', cus_comment, name='write_comment')
]
