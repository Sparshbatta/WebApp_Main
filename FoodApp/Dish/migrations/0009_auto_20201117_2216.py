# Generated by Django 3.1.3 on 2020-11-17 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dish', '0008_auto_20201117_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maindish',
            name='desc',
            field=models.TextField(max_length=400),
        ),
    ]
