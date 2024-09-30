from django.urls import path
from .views import *

urlpatterns = [
    path('home/',Homepage),

    # path('products/add/',Product_add),

    # path('products/',AllProducts),
    # path('products/delete/<int:id>/',DeleteProducts,name="product_delete"),
    # path('products/update/<int:id>/',ProductUpdate,name="product_update"),


        path('products/',AllProductsView.as_view()),
        path('products/add/',Product_addView.as_view()),
        path('products/delete/<int:id>/',DeleteProductView.as_view(),name="product_delete"),
        path('products/update/<int:id>/',ProductUpdateView.as_view(),name="product_update"),

]

