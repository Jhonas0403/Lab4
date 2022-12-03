from django import forms
from .models import Platos, Product


class DishForm(forms.ModelForm):
    class Meta:
        model = Platos
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
