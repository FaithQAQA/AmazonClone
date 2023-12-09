from django.db import models
   
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.db.models import Count

 
class TodoItem(models.Model):
     title= models.CharField(max_length=200)
     completed= models.BooleanField(default=False)
     
     
class ItemsInShop(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    left_in_stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='item_images/')
    
    @classmethod
    def get_top_selling_items(cls, limit=5):
        top_selling_items = (
            cls.objects.annotate(total_sold=Count('carts__cart_items'))
            .order_by('-total_sold')[:limit]
        )
        return top_selling_items
     
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cart_items = models.ManyToManyField('ItemsInShop', through='CartItem', related_name='carts')


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(ItemsInShop, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


