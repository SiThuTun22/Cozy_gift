# Generated by Django 5.1 on 2025-03-05 17:12

import datetime
import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name_plural": "categories",
            },
        ),
        migrations.CreateModel(
            name="Color",
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
                ("title", models.CharField(max_length=100)),
                ("color_code", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=10)),
                ("email", models.EmailField(max_length=100)),
                ("password", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Flower_Categories",
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
                ("name", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name_plural": "Flower categories",
            },
        ),
        migrations.CreateModel(
            name="FlowerStories",
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
                ("name", models.CharField(max_length=100)),
                (
                    "description",
                    models.CharField(blank=True, default="", max_length=250, null=True),
                ),
                ("image", models.ImageField(upload_to="uploads/flower/")),
                (
                    "category",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store.flower_categories",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Flower Stories",
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=100)),
                ("price", models.PositiveIntegerField(default=0)),
                (
                    "description",
                    models.CharField(blank=True, default="", max_length=250, null=True),
                ),
                ("image", models.ImageField(upload_to="uploads/product/")),
                ("is_sale", models.BooleanField(default=False)),
                (
                    "sale_price",
                    models.DecimalField(decimal_places=2, default=0, max_digits=6),
                ),
                (
                    "category",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
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
                ("quantity", models.IntegerField(default=1)),
                ("address", models.CharField(blank=True, default="", max_length=100)),
                ("phone", models.CharField(blank=True, default="", max_length=20)),
                ("date", models.DateField(default=datetime.date.today)),
                ("status", models.BooleanField(default=False)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.customer"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.product"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
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
                (
                    "date_modified",
                    models.DateTimeField(
                        auto_now=True, verbose_name=django.contrib.auth.models.User
                    ),
                ),
                ("phone", models.CharField(blank=True, max_length=20)),
                ("address1", models.CharField(blank=True, max_length=200)),
                ("address2", models.CharField(blank=True, max_length=200)),
                ("city", models.CharField(blank=True, max_length=200)),
                ("state", models.CharField(blank=True, max_length=200)),
                ("zipcode", models.CharField(blank=True, max_length=200)),
                ("country", models.CharField(blank=True, max_length=200)),
                (
                    "plaintext_password",
                    models.CharField(blank=True, max_length=128, null=True),
                ),
                ("old_cart", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
