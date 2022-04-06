from django.http import HttpResponse
from django.shortcuts import render

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


def customer(request):
    return render(request, 'accounts/customer.html')
