from django.urls import path
from . import views
from register import views as v
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/",views.todos, name="Todos"),
    path('register/',views.register_user, name='register'),
    path('items/', views.display_items, name='display_items'),
    path("cssForItems", views.display_items, name="css"),
    path("update_user/", views.update_user, name="update_user"),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),  # Replace 'cart_view' with your actual view function
    path('remove_item/<int:cart_item_id>/', views.remove_item_from_cart, name='remove_item_from_cart'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),  # Replace 'cart_view' with your actual view function
    path('contactMe/', views.contactMe, name='contactMe'),  # Replace 'cart_view' with your actual view function

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
