from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

@login_required(login_url="/")
def Customer_add(request):

    context={'customer_form':Customer_Forms()}

    if request.method == "POST":

        newcustomer= Customer_Forms(request.POST)

        if newcustomer.is_valid():

            newcustomer.save()

            return redirect('/orders/customers/add/')
    return render(request,"customers_add.html",context)



@login_required(login_url="/")
def Allcustomers(request):

    context = {
      "all_customers": Customer.objects.all()
    }

    return render(request, 'customers.html', context)
@login_required(login_url="/")
def DeleteCustomers(request, id):

    selected_product = Customer.objects.get(id = id)

    selected_product.delete()

    return redirect('/orders/customers/')
@login_required(login_url="/")
def ProductUpdate(request, id):

    selected_product = Customer.objects.get(id = id)

    context = {
        "product_form" : Customer_Forms(instance=selected_product)
    }

    if request.method == 'POST':

        product_form = Customer_Forms(request.POST, instance=selected_product)

        if product_form.is_valid():

            product_form.save()

            return redirect('/orders/customers/')

    return render(request, 'products_Add.html', context)
@login_required(login_url="/")
def Ordersadd(request):

    context =    {"order_form" : Order_Form()}

    if request.method == "POST":
        print(request.POST)

        selected_product = Product.objects.get(id=request.POST['products_reference'])

        amount = float(selected_product.price)*float(request.POST['quantity'])

        gst_amount = (amount*selected_product.gst)/100

        bill_amount = amount + gst_amount

        new_order = Orders(customer_reference_id = request.POST['customer_reference'],
                           products_reference_id = request.POST['products_reference'],
                           order_number = request.POST['order_number'],
                           order_date = request.POST['order_date'],
                           quantity = request.POST['quantity'],
                           amount = amount,
                           gst_amount = gst_amount,
                            bill_amount = bill_amount)

        new_order.save()



        return redirect('/orders/orders/add/')

    return render(request,"order_add.html",context)

@login_required(login_url="/")
def OrdersPage(request):
    context ={"all_orders":Orders.objects.all()}
    return render(request,"orders.html",context)
@login_required(login_url="/")
def OrdersDelete(request, id):

    order = Orders.objects.get(id = id)

    order.delete()

    return redirect('/orders/orders/')

@login_required(login_url="/")
def OrdersUpdate(request, id):

    order = Orders.objects.get(id = id)

    context = {
        'order_form': Order_Form(instance=order)
    }

    if request.method == 'POST':

        seleted_product = Product.objects.get(id = request.POST['products_reference'])

        amount = float(seleted_product.price) * float(request.POST['quantity'])

        gst_amount = (amount * seleted_product.gst) / 100

        bill_amount = amount + gst_amount

        order_filter = Orders.objects.filter(id = id)

        order_filter.update(customer_reference_id = request.POST['customer_reference'],
                            products_reference_id = request.POST['products_reference'],
                            order_number = request.POST['order_number'],
                            order_date = request.POST['order_date'],
                            quantity = request.POST['quantity'],
                            amount = amount,
                            gst_amount = gst_amount,
                              bill_amount = bill_amount)

        return redirect('/orders/orders/')

    return render(request, 'order_add.html', context)
