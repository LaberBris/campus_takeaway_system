from django.shortcuts import render, redirect

from customer.forms import ProfileForm, LoginForm, SignupForm
from customer.models import order_platform, Customer, UserInfo, Company, Address
import random as rd


# Create your views here.


def login(request):
    if request.session.get('is_login', None):
        print("[DEBUG][POST][STATE]:您已经登陆")
        return render(request, 'base.html', locals())

    login_form = LoginForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = UserInfo.objects.get(usr_acc=username)
                user_type_mapping = {
                    '1': 1,  # 顾客
                    '2': 2,  # 商户
                    '3': 3,  # 管理员
                }
                if user.usr_password == password:

                    if user.usrcat_id == 1:
                        request.session['usr_acc'] = user.usr_acc
                        request.session['is_login'] = True
                        user.usr_state = 1  # 更新在线状态
                        cus = Customer.objects.get(usr_acc=user.usr_acc)
                        usr_name = cus.cus_usrname
                        phone = cus.cus_phone
                        address = Address.objects.get(cus=cus).address
                        return render(request, 'customer/index.html',
                                      {'usr_name': usr_name, 'phone': phone, 'address': address})
                    elif user.usrcat_id == 2:
                        request.session['usr_acc'] = user.usr_acc
                        request.session['is_login'] = True
                        user.usr_state = 1  # 更新在线状态
                        cmp = Company.objects.get(usr_acc=user.usr_acc)
                        cmpname = cmp.cmp_name
                        cmptel = cmp.cmp_tel
                        print("[DEBUG][POST][STATE]:cmpname:{}".format(cmpname))
                        return render(request, 'company/company_base.html',
                                      {'cmpname': cmpname, 'phone': cmptel})
                else:
                    return render(request, 'customer/login.html', {'login_form': login_form, 'error': '密码错误!'})
            except UserInfo.DoesNotExist:
                return render(request, 'customer/login.html',
                              {'login_form': login_form, 'error': '用户不存在!请先注册'})
    return render(request, 'customer/login.html', {'login_form': login_form})


def signup(request):
    signup_form = SignupForm()
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            username = signup_form.cleaned_data['username']
            password = signup_form.cleaned_data['password']
            password2 = signup_form.cleaned_data['password2']
            phone = signup_form.cleaned_data['phone']
            # 使用字典将用户类型映射为整数值
            user_type_mapping = {
                '1': 1,  # 顾客
                '2': 2,  # 商户
                '3': 3,  # 管理员
            }
            userType = user_type_mapping[signup_form.cleaned_data['userType']]

            if password == password2:
                try:
                    user = UserInfo.objects.get(usr_acc=username)
                    print(userType)
                    return render(request, 'customer/signup.html', {'error': '用户已存在!'})
                except UserInfo.DoesNotExist:
                    if userType == 1:
                        user = UserInfo(usr_acc=username, usr_password=password, usrcat_id=1, usr_state=0)
                        user.save()
                        customer = Customer.objects.create(usr_acc=user, cus_usrname='顾客' + str(rd.randint(1, 1000)),
                                                           cus_phone=phone)
                        address = Address.objects.create(cus=customer, address='未设置')
                    elif userType == 2:
                        user = UserInfo(usr_acc=username, usr_password=password, usrcat_id=2, usr_state=0)
                        user.save()
                        company = Company.objects.create(usr_acc=user, cmp_name='商家' + str(rd.randint(1, 1000)),
                                                         cmp_tel=phone)
                    else:
                        return render(request, 'admin', {'error': '管理员请用admin登录'})
                    return render(request, 'customer/login.html', locals())
            else:
                error = '两次输入的密码不一致'

    return render(request, 'customer/signup.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return render(request, 'customer/logout.html', locals())
    user_acc = request.session['usr_acc']
    print("[DEBUG][REQUEST][退出]]")
    print("[DEBUG][REQUEST][usr_acc]:{}".format(user_acc))
    try:
        user = UserInfo.objects.get(usr_acc=user_acc)
        print("[DEBUG][REQUEST][退出]]：退出顾客身份")
        user.usr_state = 0  # 更新离线状态
        user.save()
        message = '已登出,请重新登录或重新注册'
    except UserInfo.DoesNotExist:
        message = '用户不存在'

    request.session.flush()
    return render(request, 'customer/logout.html', locals())


def index(request):
    # 从数据库中获取用户信息
    user_acc = request.session['usr_acc']
    user = UserInfo.objects.get(usr_acc=user_acc)
    customer = Customer.objects.get(usr_acc=user)
    user_name = customer.cus_usrname
    phone = customer.cus_phone
    addr = Address.objects.get(cus=customer).address
    # print(11111, "index", addr)
    return render(request, 'customer/address.html',
                  {'user': user, 'username': user_name, 'phone': phone, 'address': addr})


def address(request):
    # 判断用户是否登录
    profile_form = ProfileForm()
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            user_acc = request.session['usr_acc']
            user_name = profile_form.cleaned_data['username']
            phone = profile_form.cleaned_data['phone']
            cus_address = profile_form.cleaned_data['address']

            try:
                user = UserInfo.objects.get(usr_acc=user_acc)
                cus = Customer.objects.get(usr_acc=user)
                cus.cus_usrname = user_name
                cus.cus_phone = phone
                addr = Address.objects.get(cus=cus)
                addr.address = cus_address
                addr.save()
                cus.save()

                return render(request, 'customer/index.html',
                              {'user': user, 'usr_name': user_name, 'phone': phone, 'address': cus_address})
            except UserInfo.DoesNotExist:
                message = '用户不存在'
    return render(request, 'customer/index.html', locals())
