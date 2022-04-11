from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from crm_ivy_django.accounts.models import Order

AppUser = get_user_model()


class OrderCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ['username', 'email', 'password1', 'password2']
