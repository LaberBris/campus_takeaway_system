# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    address_id = models.IntegerField(primary_key=True)
    cus = models.ForeignKey('Customer', models.DO_NOTHING)
    address = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'address'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Canteen(models.Model):
    ct_id = models.IntegerField(primary_key=True)
    ct_name = models.CharField(max_length=50, db_collation='utf8mb3_general_ci')

    class Meta:
        managed = False
        db_table = 'canteen'


class Comment(models.Model):
    cmt_id = models.IntegerField(primary_key=True)
    st = models.ForeignKey('Store', models.DO_NOTHING)
    od = models.ForeignKey('Orders', models.DO_NOTHING, blank=True, null=True)
    cmt_star = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cmt_content = models.CharField(max_length=1024, blank=True, null=True)
    cmt_image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'


class Company(models.Model):
    cmp_id = models.IntegerField(primary_key=True)
    usr_acc = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='usr_acc', blank=True, null=True)
    cmp_name = models.CharField(max_length=50)
    cmp_tel = models.DecimalField(max_digits=12, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'company'


class Customer(models.Model):
    cus_id = models.IntegerField(primary_key=True)
    usr_acc = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='usr_acc')
    cus_usrname = models.CharField(max_length=20)
    cus_phone = models.DecimalField(max_digits=12, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'customer'


class Dish(models.Model):
    dish_id = models.IntegerField(primary_key=True)
    st = models.ForeignKey('Store', models.DO_NOTHING)
    dish_name = models.CharField(max_length=20)
    dish_price = models.FloatField()
    dish_deliver = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    dish_image = models.TextField(blank=True, null=True)
    # dish_image = models.ImageField(upload_to='./static/images', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dish'


class DishAmount(models.Model):
    od = models.OneToOneField('Orders', models.DO_NOTHING, primary_key=True)
    dish = models.ForeignKey(Dish, models.DO_NOTHING)
    oder_dish_amount = models.DecimalField(max_digits=2, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'dish_amount'
        unique_together = (('od', 'dish'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Manager(models.Model):
    mn_id = models.IntegerField(primary_key=True)
    ct = models.ForeignKey(Canteen, models.DO_NOTHING)
    usr_acc = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='usr_acc', blank=True, null=True)
    mn_name = models.CharField(max_length=20)
    mn_phone = models.DecimalField(max_digits=12, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'manager'


class Orders(models.Model):
    od_id = models.IntegerField(primary_key=True)
    cus = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    address = models.ForeignKey(Address, models.DO_NOTHING, blank=True, null=True)
    od_time = models.DateTimeField()
    od_money = models.FloatField()
    od_state = models.DecimalField(max_digits=1, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'orders'


class Store(models.Model):
    st_id = models.IntegerField(primary_key=True)
    ct = models.ForeignKey(Canteen, models.DO_NOTHING)
    cmp = models.ForeignKey(Company, models.DO_NOTHING)
    st_name = models.CharField(max_length=50)
    st_tel = models.DecimalField(max_digits=8, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'store'


class UserInfo(models.Model):
    usr_acc = models.CharField(primary_key=True, max_length=12)
    usrcat = models.ForeignKey('Usercategory', models.DO_NOTHING)
    usr_state = models.DecimalField(max_digits=1, decimal_places=0)
    usr_password = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'user_info'


class Usercategory(models.Model):
    usrcat_id = models.IntegerField(primary_key=True)
    usrcat_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'usercategory'


class order_platform(models.Model):
    ct_name = models.CharField(max_length=50)
    st_name = models.CharField(max_length=50)
    dish_name = models.CharField(max_length=20)
    dish_price = models.FloatField()
    dish_deliver = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    dish_image = models.TextField(blank=True, null=True)
    st_tel = models.DecimalField(max_digits=8, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'order_platform'

