# Generated by Django 4.2.4 on 2023-08-22 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_publication_price_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='publication',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='price',
        ),
    ]