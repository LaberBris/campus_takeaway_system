# Generated by Django 4.1 on 2023-10-28 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("customer", "0002_alter_customer_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="usr_acc",
            field=models.ForeignKey(
                db_column="usr_acc",
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="customer.userinfo",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="customer",
            name="cus_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
