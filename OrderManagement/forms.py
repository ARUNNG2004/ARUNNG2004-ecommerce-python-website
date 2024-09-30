# from django.forms import ModelForm
from django import forms
from .models import *

class Customer_Forms(forms.ModelForm):

    class Meta:

        model = Customer
        fields = '__all__'

class Order_Form(forms.ModelForm):

    class Meta:

        model = Orders
        fields = ['customer_reference','products_reference','order_number','order_date','quantity']
