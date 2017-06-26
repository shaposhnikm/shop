from django import forms

from .models import Product

from .models import Order


class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ( 
			'price',
		)

class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ( 
			'first_name',
			'last_name',
			'email',
		)