from django import forms

from django.contrib.auth import get_user_model
User = get_user_model()

from product.models import Product
from .models import Order, OrderItem


class OrderForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        label='用户',
        queryset=User.objects.using('auth_db')
    )

    class Meta:
        model = Order
        fields = '__all__'


class OrderItemForm(forms.ModelForm):
    product = forms.ModelChoiceField(
        label='产品',
        queryset=Product.objects.using('primary')
    )

    class Meta:
        model = OrderItem
        fields = '__all__'
