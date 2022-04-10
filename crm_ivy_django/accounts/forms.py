from django import forms

from crm_ivy_django.accounts.models import Order


class OrderCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
