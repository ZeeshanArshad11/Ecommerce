from django import forms


from .models import Address

class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		fields = [
		#'billing_profile',
		#'address_type',
		'address_line_1',
		'address_line_2',
		'city',
		'state',
		'country',
		'postal_code'
		]
		#fields = '__all__'

	# 	address_line_1 = forms.CharField( 
	# 	label='',
	# 	widget=forms.TextInput(
	# 		attrs={
	# 			"class": "form-control mb-4",
	# 			"placeholder": "Address Line 1",

	# 		}
	# 	)
	# )
	# 	address_line_2 = forms.CharField( 
	# 	label='',
	# 	widget=forms.TextInput(
	# 		attrs={
	# 			"class": "form-control mb-4",
	# 			"placeholder": "Address Line 2",

	# 		}
	# 	)
	# )
	# 	city = forms.CharField( 
	# 	label='',
	# 	widget=forms.TextInput(
	# 		attrs={
	# 			"class": "form-control mb-4",
	# 			"placeholder": "City",

	# 		}
	# 	)
	# )
	# 	state = forms.CharField( 
	# 	label='',
	# 	widget=forms.TextInput(
	# 		attrs={
	# 			"class": "form-control mb-4",
	# 			"placeholder": "State",

	# 		}
	# 	)
	# )
	# 	country = forms.CharField( 
	# 	label='',
	# 	widget=forms.TextInput(
	# 		attrs={
	# 			"class": "form-control mb-4",
	# 			"placeholder": "Country",

	# 		}
	# 	)
	# )
	# 	postal_code = forms.CharField( 
	# 	label='',
	# 	widget=forms.TextInput(
	# 		attrs={
	# 			"class": "form-control mb-4",
	# 			"placeholder": "Postal Code",

	# 		}
	# 	)
	# )
