from django import forms
from django.contrib.auth import get_user_model



User = get_user_model()



class ContactForm(forms.Form):
	name = forms.CharField( 
		label='',
		widget=forms.TextInput(
			attrs={
				"class": "form-control mb-4",
				"placeholder": "Name",

			}
		)
	)
	email = forms.EmailField( 
		label='',
		widget=forms.TextInput(
			attrs={
				"class": "form-control mb-4",
				"placeholder": "E-mail",

			}
		)
	)
	Subject_CHOICES =( 
		("", "Choose Option"),
    	("feedback", "Feedback"), 
    	("bug", "Report a bug"), 
    	("feature", "Feature request"), 

	)
	subject = forms.ChoiceField(
		label='Subject',
		choices=Subject_CHOICES,
		widget=forms.Select(
			attrs={
				"class": "form-control browser-default custom-select mb-4",

			}
			)

		)
		
	message = forms.CharField(
		label='',
		widget=forms.Textarea(
			attrs={
				"class": "form-control rounded-0 mb-4",
				"placeholder": "Message",
				"rows":"4"

			}
		))


