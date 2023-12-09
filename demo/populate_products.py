# Assuming this script resides in the same directory as your Django app

import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")
django.setup()

from myapp.models import ItemsInShop

# Sample products data
products_data = [
    {
        'title': 'iPhone 13 Pro',
        'cost': 1099.99,
        'left_in_stock': 30,
        'image': 'item_images/iphone13pro.jpg',
    },
    {
        'title': 'Samsung Galaxy S21',
        'cost': 899.99,
        'left_in_stock': 40,
        'image': 'item_images/samsunggalaxys21.jpg',
    },
    {
        'title': 'Dell XPS 15 Laptop',
        'cost': 1399.99,
        'left_in_stock': 25,
        'image': 'item_images/dellxps15.jpg',
    },
    {
        'title': 'Sony WH-1000XM4 Headphones',
        'cost': 349.99,
        'left_in_stock': 50,
        'image': 'item_images/sonywh1000xm4.jpg',
    },
    {
        'title': 'Canon EOS R5 Camera',
        'cost': 3799.99,
        'left_in_stock': 15,
        'image': 'item_images/canoneosr5.jpg',
    },
    {
        'title': 'Apple AirPods Pro',
        'cost': 249.99,
        'left_in_stock': 60,
        'image': 'item_images/airpodspro.jpg',
    },
    {
        'title': 'LG OLED55C1PUB TV',
        'cost': 1799.99,
        'left_in_stock': 10,
        'image': 'item_images/lgoled55c1pub.jpg',
    },
    {
        'title': 'Nintendo Switch Console',
        'cost': 299.99,
        'left_in_stock': 20,
        'image': 'item_images/nintendoswitch.jpg',
    },
    {
        'title': 'Bose QuietComfort 45 Headphones',
        'cost': 329.99,
        'left_in_stock': 30,
        'image': 'item_images/boseqc45.jpg',
    },
    {
        'title': 'ASUS ROG Strix G15 Gaming Laptop',
        'cost': 1599.99,
        'left_in_stock': 18,
        'image': 'item_images/asusrogstrixg15.jpg',
    },
]

# Creating and saving instances of ItemsInShop
for product_data in products_data:
    new_product = ItemsInShop.objects.create(
        title=product_data['title'],
        cost=product_data['cost'],
        left_in_stock=product_data['left_in_stock'],
        image=product_data['image']
    )
    new_product.save()
