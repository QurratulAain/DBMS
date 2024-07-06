#created new
from django import forms
from .models import Orders

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['order_id', 'payment_method', 'items', 'items_numbering', 'quantity_of_items','unit_price']
