# Generated by Django 5.1 on 2025-03-07 17:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("store", "0002_product_color_alter_flowerstories_category_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
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
                ("full_name", models.CharField(max_length=250)),
                ("email", models.EmailField(max_length=250)),
                ("shipping_address", models.TextField(max_length=150000)),
                ("amount_paid", models.DecimalField(decimal_places=2, max_digits=7)),
                ("date_ordered", models.DateTimeField(auto_now_add=True)),
                ("shipped", models.BooleanField(default=False)),
                ("date_shipped", models.DateTimeField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
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
                ("quantity", models.PositiveBigIntegerField(default=1)),
                ("price", models.DecimalField(decimal_places=2, max_digits=7)),
                (
                    "order",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="payment.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ShippingAddress",
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
                ("shipping_full_name", models.CharField(max_length=255)),
                ("shipping_email", models.CharField(max_length=255)),
                ("shipping_address1", models.CharField(max_length=255)),
                (
                    "shipping_address2",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("shipping_city", models.CharField(max_length=255)),
                (
                    "shipping_state",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "shipping_zipcode",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("shipping_country", models.CharField(max_length=255)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Shipping Address",
            },
        ),
    ]
