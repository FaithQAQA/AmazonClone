from django.contrib import admin
from .models import TodoItem , ItemsInShop, Cart, CartItem
# Register your models here.
admin.site.register(TodoItem)
admin.site.register(ItemsInShop)
admin.site.register(Cart)
admin.site.register(CartItem)