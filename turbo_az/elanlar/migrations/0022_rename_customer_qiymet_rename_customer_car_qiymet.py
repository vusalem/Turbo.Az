# Generated by Django 5.0.7 on 2024-09-21 05:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("elanlar", "0021_rename_dealer_şeher"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Customer",
            new_name="Qiymet",
        ),
        migrations.RenameField(
            model_name="car",
            old_name="customer",
            new_name="qiymet",
        ),
    ]
