from django.shortcuts import redirect, render , HttpResponse
from requests import request
from .models import TodoItem , ItemsInShop
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render , get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from register.forms import SignUpForm
from django.http import HttpResponse
from django.template import loader
from .models import ItemsInShop, CartItem
from .models import Cart
from django.http import HttpResponseRedirect

def home(request):
    return render(request, "home.html")

def contactMe(request):
    return render(request,"contact.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def display_items(request):
    items = ItemsInShop.objects.all() 
    return render(request, 'Items.html', {'items': items})


def update_user(request):
    if request.user.is_authenticated:
            current_user = User.objects.get(id=request.user.id)
            form = SignUpForm(request.POST or None , instance=current_user)
            
            if form.is_valid():
                form.save()
                login(request, current_user)
                messages.success(request, ("Profile has been updated!.."))
                return redirect('home')
            return render(request, "profile.html", {'form':form})
    else:
            messages.success(request, "You Must Be Logged In to See This Page...")
            return render(request, "registration/login.html", {'messages': messages.get_messages(request)})
        
from django.shortcuts import get_object_or_404, redirect
from .models import ItemsInShop

def add_to_cart(request, item_id):
    item = get_object_or_404(ItemsInShop, pk=item_id)
    quantity = 1  

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))

    if request.user.is_authenticated:
        user_cart, created = Cart.objects.get_or_create(user=request.user)

        if quantity > item.left_in_stock:
            messages.error(request, "Not enough items in stock.")
            return redirect('item_detail', item_id=item_id)  

        cart_item, created = CartItem.objects.get_or_create(cart=user_cart, item=item)
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
            messages.success(request, f"Updated {item.title} quantity in cart.")
        else:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, f"Added {item.title} to cart.")

        return redirect('cart')  
    else:
       
        return redirect('login')  


    

def view_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = cart.cartitem_set.all()  
        total_cost = sum(item.item.cost * item.quantity for item in cart_items)
        return render(request, 'cart.html', {'cart_items': cart_items, 'total_cost': total_cost})
    
    
def remove_item_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    cart_item.delete()
    return HttpResponseRedirect('/cart/') 

def clear_cart(request):
    if request.user.is_authenticated:
        user_cart_items = CartItem.objects.filter(cart__user=request.user)
        user_cart_items.delete()
        return redirect('cart')  
    else:
       
        return redirect('login')  
    
    
    
    
def register_user(request):
    form = SignUpForm()
    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            password= form.cleaned_data['password1']
          

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,("You had made an account"))
            return redirect('home')
        
    return render(request, "register.html", {'form':form})
