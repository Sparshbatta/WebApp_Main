# Generated by Django 3.1.3 on 2020-11-25 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dish', '0010_auto_20201117_2217'),
        ('Order', '0005_auto_20201125_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cuisine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dish.maindish'),
        ),
    ]
