# Generated by Django 3.1.3 on 2020-11-16 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cust', '0005_auto_20201116_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='image',
            field=models.FileField(upload_to='clients/images/'),
        ),
    ]
