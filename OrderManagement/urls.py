from django.urls import path
from .views import *

urlpatterns = [

    path('customers/add/',Customer_add),
    path('customers/',Allcustomers),
    path('customers/delete/<int:id>/',DeleteCustomers,name="customers_delete"),
    path('customers/update/<int:id>/',ProductUpdate,name="customers_update"),

    path('orders/',OrdersPage),
    path('orders/add/',Ordersadd),
    path('orders/delete/<int:id>/',OrdersDelete,name="order_delete"),
    path('orders/update/<int:id>/',OrdersUpdate,name="order_update"),
]

