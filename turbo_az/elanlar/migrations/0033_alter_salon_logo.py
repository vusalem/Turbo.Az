# Generated by Django 5.0.7 on 2024-09-25 19:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("elanlar", "0032_alter_salon_logo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="salon",
            name="logo",
            field=models.ImageField(upload_to="elanlar/movie/logos"),
        ),
    ]
