from django import forms
from .models import Order, Email, Item

class AddOrder(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['order_time']

class AddEmail(forms.ModelForm):
    class Meta:
        model = Email
        fields = '__all__'

class AddItem(forms.ModelForm):
    class Meta:
        model = Item     
        fields = '__all__'