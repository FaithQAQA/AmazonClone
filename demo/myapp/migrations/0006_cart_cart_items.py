# Generated by Django 4.2.7 on 2023-12-08 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_cartitem_user_cart_cartitem_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cart_items',
            field=models.ManyToManyField(related_name='carts', through='myapp.CartItem', to='myapp.itemsinshop'),
        ),
    ]
