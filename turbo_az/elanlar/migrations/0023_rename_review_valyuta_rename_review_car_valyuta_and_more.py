# Generated by Django 5.0.7 on 2024-09-21 05:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("elanlar", "0022_rename_customer_qiymet_rename_customer_car_qiymet"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Review",
            new_name="Valyuta",
        ),
        migrations.RenameField(
            model_name="car",
            old_name="review",
            new_name="valyuta",
        ),
        migrations.RenameField(
            model_name="car",
            old_name="dealer",
            new_name="şeher",
        ),
    ]
