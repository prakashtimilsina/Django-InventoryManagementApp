from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput

from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_id': 'Product ID',
            'name': 'Product Name',
            'sku': 'SKU',
            'price': 'Product Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier',
        }
        widgets = {
            'product_id': forms.NumberInput(
                attrs={'placeholder':'e.g. 1', 'class':'form-control'}),
            'name': forms.TextInput(
                attrs={'placeholder':'e.g. shirt', 'class':'form-control'}),
            'sku': forms.TextInput(
                attrs={'placeholder':'e.g. S12345', 'class':'form-control'}),
            'price': forms.NumberInput(
                attrs={'placeholder':'e.g. 19.99', 'class':'form-control'}),
            'quantity': forms.NumberInput(
                attrs={'placeholder':'e.g. 12', 'class':'form-control'}),
            'supplier': forms.TextInput(
                attrs={'placeholder':'e.g. ABC Corp', 'class':'form-control'}),
        }

# - Register/Create a User
class CreateUserForm(UserCreationForm):
    class Meta:
        
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())        
    password = forms.CharField(widget=PasswordInput())  

      