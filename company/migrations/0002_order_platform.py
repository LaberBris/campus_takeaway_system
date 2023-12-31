# Generated by Django 4.1 on 2023-10-28 06:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("company", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="order_platform",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ct_name", models.CharField(max_length=50)),
                ("st_name", models.CharField(max_length=50)),
                ("dish_name", models.CharField(max_length=20)),
                ("dish_price", models.FloatField()),
                (
                    "dish_deliver",
                    models.DecimalField(
                        blank=True, decimal_places=0, max_digits=1, null=True
                    ),
                ),
                ("dish_image", models.TextField(blank=True, null=True)),
                ("st_tel", models.DecimalField(decimal_places=0, max_digits=8)),
            ],
            options={
                "db_table": "order_platform",
                "managed": False,
            },
        ),
    ]
