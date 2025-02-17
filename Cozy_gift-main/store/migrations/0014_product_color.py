# Generated by Django 5.1 on 2025-02-06 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0013_profile_plaintext_password"),
    ]

    operations = [
        migrations.AddField(
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
                ],
                default="Blue",
                max_length=50,
                null=True,
            ),
        ),
    ]
