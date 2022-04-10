from django.urls import path

from crm_ivy_django.accounts.views import home, products, customer, order_create, order_edit, order_delete

urlpatterns = [
    path('', home, name='index'),
    path('products/', products, name='products'),
    path('customer/<int:pk>/', customer, name='customers'),

    path('order_create/', order_create, name='order create'),
    path('order_edit/<int:pk>/', order_edit, name='order edit'),
    path('order_delete/<int:pk>/', order_delete, name='order delete'),
]
