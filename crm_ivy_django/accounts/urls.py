from django.urls import path

from crm_ivy_django.accounts.views import home, products, customer, order_create, order_edit, order_delete, \
    register_page, login_page, logout_page

urlpatterns = [
    path('', home, name='index'),
    path('products/', products, name='products'),
    path('customer/<int:pk>/', customer, name='customers'),

    path('order_create/<int:pk>/', order_create, name='order create'),
    path('order_edit/<int:pk>/', order_edit, name='order edit'),
    path('order_delete/<int:pk>/', order_delete, name='order delete'),

    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
]
