# Generated by Django 5.1 on 2025-02-06 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0014_product_color"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="color",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Blue", "Blue"),
                    ("Cream", "Cream"),
                    ("Green", "Green"),
                    ("Pink", "Pink"),
                    ("Red", "Red"),
                    ("White", "White"),
                    ("Purple", "Purple"),
                ],
                default="Blue",
                max_length=50,
                null=True,
            ),
        ),
    ]
