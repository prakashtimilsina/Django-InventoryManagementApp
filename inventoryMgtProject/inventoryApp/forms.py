from django import forms 
from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_id' : 'Product ID',
            'name' : 'Product Name',
            'sku' : 'SKU',
            'price' : 'Product Price',
            'quantity' : 'Product Quantity',
            'supplier' : 'Supplier',
        }
        widgets = {
            'product_id' : forms.NumberInput(attrs={'placeholder': 'e.g. 1', 'class': 'form-control' }),
            'name' : forms.TextInput(attrs={'placeholder': 'e.g. Shirt', 'class': 'form-control' }),
            'sku' : forms.TextInput(attrs={'placeholder': 'e.g. s12402', 'class': 'form-control' }),
            'price' : forms.NumberInput(attrs={'placeholder': 'e.g. 19.20', 'class': 'form-control' }),
            'quantity' : forms.NumberInput(attrs={'placeholder': 'e.g. 12', 'class': 'form-control' }),
            'supplier' : forms.TextInput(attrs={'placeholder': 'e.g. Abc llc.', 'class': 'form-control' }),
        }