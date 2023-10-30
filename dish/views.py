from time import sleep

from django.shortcuts import render, redirect
from datetime import datetime
from customer.models import Dish, Orders, DishAmount, Customer, Address, Comment, Store


# Create your views here.
def dish(request):
    dishes = Dish.objects.all()

    if request.method == 'POST':
        money = 0

        # 获取当前用户信息
        usr_acc = request.session.get('usr_acc')
        customer = Customer.objects.get(usr_acc=usr_acc)
        address = Address.objects.get(cus=customer)
        time = datetime.now()
        Orders.objects.create(cus=customer, address=address, od_state=0, od_money=0.00, od_time=time)

        order = Orders.objects.last()
        print("[DEBUG][POST][STATE]:order:{}".format(order))

        for dish in dishes:  # 假设这里是您的菜品列表
            dish_id = dish.dish_id
            dish_price = dish.dish_price
            dish_num = request.POST.get('dish_num_' + str(dish_id))

            money += dish_price * int(dish_num)
            DishAmount.objects.create(od=order, dish=dish, oder_dish_amount=dish_num)

        order.od_money = round(money, 2)
        order.save()

        orders = Orders.objects.filter(cus=customer)
        dishes = DishAmount.objects.filter(od__in=orders)

        return render(request, 'customer/comment.html', locals())

    return render(request, 'dish.html', locals())


def comment(request):
    user = request.session.get('usr_acc')
    customer = Customer.objects.get(usr_acc=user)
    orders = Orders.objects.filter(cus=customer)
    dishes = DishAmount.objects.filter(od__in=orders)

    if request.method == 'POST':
        comment_order = request.POST['comment_order']
        print("[DEBUG][POST][STATE]:comment_order:{}".format(comment_order))

        return render(request, 'customer/cus_comment.html', {'comment_order': comment_order, 'dishes': dishes})

    return render(request, 'customer/comment.html', locals())


def cus_comment(request):
    user = request.session.get('usr_acc')
    customer = Customer.objects.get(usr_acc=user)
    orders = Orders.objects.filter(cus=customer)
    dishes = DishAmount.objects.filter(od__in=orders)

    if request.method == 'POST':
        comment_order = request.POST.get('comment_order')
        comment_star = request.POST['comment_star']
        comment_content = request.POST['comment_content']
        order = Orders.objects.get(od_id=comment_order)
        dishes = DishAmount.objects.filter(od=order)
        store = dishes.last().dish.store
        Comment.objects.create(od=order, st=store, cmt_star=comment_star, cmt_content=comment_content)

        return render(request, 'customer/comment.html', locals())

    return render(request, 'customer/comment.html', locals())