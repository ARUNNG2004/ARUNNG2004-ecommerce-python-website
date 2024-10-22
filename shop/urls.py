from django.urls import path
from . import views
urlpatterns =[
path('',views.home,name="home"),
path('register',views.register,name="register"),
path('login',views.loginpage,name="login"),
path('logout',views.logout_page,name="logout"),

path('collections',views.collections,name="collections"),
path('addtocart',views.add_to_cart,name="addtocart"),
path('cart',views.cart,name="cart"),

path('collections/<str:name>',views.collectionsview,name="collections"),

path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),

path('collections/<str:cname>/<str:pname>',views.product_details,name="product_details"),
]
