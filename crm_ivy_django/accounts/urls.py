from django.urls import path

from crm_ivy_django.accounts.views import home, products, customer

urlpatterns = [
    path('', home, name='index'),
    path('products/', products, name='products'),
    path('customer/<int:pk>/', customer, name='customers'),
]
