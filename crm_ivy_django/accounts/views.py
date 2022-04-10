from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect

from crm_ivy_django.accounts.forms import OrderCreateUpdateForm
from crm_ivy_django.accounts.models import Customer, Order, Product


def home(request):
    all_customers = Customer.objects.all()
    all_orders = Order.objects.all()

    orders_count = all_orders.count()
    delivered_orders = all_orders.filter(status='Delivered').count()
    pending_orders = all_orders.filter(status='Pending').count()

    context = {
        'all_customers': all_customers,
        'all_orders': all_orders,
        'orders_count': orders_count,
        'delivered_orders': delivered_orders,
        'pending_orders': pending_orders,
    }

    return render(request, 'accounts/dashboard.html', context)


def products(request):
    all_products = Product.objects.all()

    context = {
        'all_products': all_products,
    }
    return render(request, 'accounts/products.html', context)


def customer(request, pk):
    current_customer = Customer.objects.get(id=pk)
    customer_orders = current_customer.order_set.all()
    orders_count = customer_orders.count()

    context = {
        'current_customer': current_customer,
        'customer_orders': customer_orders,
        'orders_count': orders_count,
    }
    return render(request, 'accounts/customer.html', context)


def order_create(request, pk):
    # form = OrderCreateUpdateForm()
    formset_factory = inlineformset_factory(Customer, Order, fields=('products', 'status'))
    current_customer = Customer.objects.get(id=pk)
    formset = formset_factory(queryset=Order.objects.none(), instance=current_customer)
    # form.initial = {
    #     'customer': current_customer,
    # }

    if request.method == 'POST':
        formset = formset_factory(request.POST, instance=current_customer)
        if formset.is_valid():
            formset.save()
            return redirect('index')

    context = {
        'formset': formset,
        'current_customer': current_customer,
    }
    return render(request, 'accounts/order_create_update.html', context)


def order_edit(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderCreateUpdateForm(instance=order)

    if request.method == 'POST':
        form = OrderCreateUpdateForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'accounts/order_create_update.html', context)


def order_delete(request, pk):
    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('index')

    context = {
        'order': order,
    }

    return render(request, 'accounts/order_delete.html', context)
