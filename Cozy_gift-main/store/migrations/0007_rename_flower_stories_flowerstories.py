# Generated by Django 5.1 on 2025-01-11 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0006_rename_flowerstories_flower_stories_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="flower_stories",
            new_name="FlowerStories",
        ),
    ]
