# Generated by Django 4.2.4 on 2023-08-21 06:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0002_cartmodel_quantity_alter_cartmodel_products_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartmodel',
            name='user',
        ),
        migrations.CreateModel(
            name='Cart_fath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
