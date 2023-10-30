import base64

from django.shortcuts import render, redirect, get_object_or_404

from .models import Company, Store, UserInfo, Dish, Orders, DishAmount


def cmp_manage(request):
    if not request.session.get('is_login', None):
        print("[DEBUG] 尚未登录")
        message = '尚未登录,请登录'
        return render(request, "Company/company_base.html", locals())
    if request.method == 'GET' or request.method == 'POST':
        usr_acc = request.session['usr_acc']
        if usr_acc is not None:
            user = UserInfo.objects.get(usr_acc=usr_acc)
            usr_cat = user.usrcat_id
            # print("*************************", usr_cat)
            if usr_cat != 2:
                error = '您不是商家!无法进行商家管理!请先登出后用商家账户登录!'
                for value, key in request.session.items():
                    print('key: %s value: %s' % (value, key))
                return render(request, 'customer/login.html', locals())

            company = Company.objects.get(usr_acc=usr_acc)
            cmpname = company.cmp_name
            for value, key in request.session.items():
                print('key: %s value: %s' % (value, key))
            return render(request, 'company/company_base.html', {'cmpname': cmpname})
    return render(request, 'company/company_base.html', locals())


def cmp_store(request):
    usr_acc = request.session['usr_acc']
    if usr_acc is not None:
        cmp_id = Company.objects.get(usr_acc=usr_acc).cmp_id
        stores = Store.objects.filter(cmp_id=cmp_id)

    if request.method == 'POST':
        # 处理添加商铺的逻辑
        if 'st_name' in request.POST and 'ct_id' in request.POST and 'st_tel' in request.POST:
            st_name = request.POST['st_name']
            ct_id = request.POST['ct_id']
            st_tel = request.POST['st_tel']
            Store.objects.create(st_name=st_name, ct_id=ct_id, st_tel=st_tel, cmp_id=cmp_id)

        # 处理删除商铺的逻辑
        if 'store_id' in request.POST:
            store_id = request.POST['store_id']
            store = get_object_or_404(Store, st_id=store_id)
            store.delete()

        return render(request, 'company/cmp_store.html', {'stores': stores})

    return render(request, 'company/cmp_store.html', {'stores': stores})


def cmp_dish(request):
    usr_acc = request.session['usr_acc']

    if usr_acc is not None:
        cmp_id = Company.objects.get(usr_acc=usr_acc).cmp_id
        stores = Store.objects.filter(cmp_id=cmp_id)
        dishes = Dish.objects.filter(st_id__in=stores)

    if request.method == 'POST':
        # 处理添加菜品
        if 'st_id' in request.POST and 'dish_name' in request.POST and 'dish_price' in request.POST:
            st_id = request.POST['st_id']
            dish_name = request.POST['dish_name']
            dish_price = request.POST['dish_price']
            # dish_image = request.FILES['dish_image'].read()
            # print("***************", request.POST['dish_deliver'])
            dish_deliver_map = {
                '1': 1,
                '0': 0
            }
            # for key, value in request.POST.items():
                # print(f"Key: {key}, Value: {value}")
            dish_deliver = int(request.POST['dish_deliver'])
            Dish.objects.create(st_id=st_id, dish_name=dish_name, dish_price=dish_price, dish_image=None, dish_deliver=1)

        # 处理删除菜品
        if 'dish_id' in request.POST:
            dish_id = request.POST['dish_id']
            dish = get_object_or_404(Dish, dish_id=dish_id)
            dish.delete()

    return render(request, 'company/cmp_dish.html', {'dishes': dishes})


def cmp_order(request):
    usr_acc = request.session['usr_acc']
    if usr_acc is not None:
        cmp_id = Company.objects.get(usr_acc=usr_acc).cmp_id
        stores = Store.objects.filter(cmp_id=cmp_id)
        dishes = Dish.objects.filter(st_id__in=stores)
        dishamount = DishAmount.objects.filter(dish_id__in=dishes)
        # 创建一个上下文对象orders,将dishamount中含有的所有dish_id填入
        orders = Orders.objects.filter(od_id__in=dishamount)
        print("**************", dishamount)

    if request.method == 'POST':
        # 处理接单
        if 'order_id' in request.POST:
            order_id = request.POST['order_id']
            order = get_object_or_404(Orders, od_id=order_id)
            order.od_state = 1
            order.save()

    return render(request, 'company/cmp_order.html', {'dishes': dishamount, 'orders': orders, 'dish_list': dishes})


