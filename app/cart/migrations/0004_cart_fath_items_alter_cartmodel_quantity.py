# Generated by Django 4.2.4 on 2023-08-21 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_remove_cartmodel_user_cart_fath'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_fath',
            name='items',
            field=models.ManyToManyField(to='cart.cartmodel'),
        ),
        migrations.AlterField(
            model_name='cartmodel',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
