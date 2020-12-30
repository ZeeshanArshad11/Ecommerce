from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()

class GuestForm(forms.Form):
	email = forms.EmailField(
		label='',
		widget=forms.TextInput(
			attrs={
				"class": "form-control mb-4",
				"placeholder": "E-mail",

			}
		)
		)


class LoginForm(forms.Form):
	username = forms.CharField(
		label='',
		widget=forms.TextInput(
			attrs={
				"class": "form-control mb-4",
				"placeholder": "User Name",

			}
		)
		)
	password = forms.CharField(
		label='',
		widget=forms.PasswordInput(
			attrs={
				"class": "form-control mb-4",
				"placeholder": "***********",

			}
		)
		)



class RegisterForm(forms.Form):
	username = forms.CharField(
		label='',
		widget=forms.TextInput(
			attrs={
				"class": "form-control mb-4",
				"placeholder": "User Name",

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
	password = forms.CharField(
		label='',
		widget=forms.PasswordInput(
			attrs={
				"class": "form-control mb-4",
				"placeholder": "***********",

			}
		)
		)
	password2 = forms.CharField(
		label='',
		widget=forms.PasswordInput(
			attrs={
				"class": "form-control mb-4",
				"placeholder": "Confirm Password",

			}
		)
		)
	def clean_username(self):
		username = self.cleaned_data.get("username")
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError('Username is already taken')
		return username

	def clean_email(self):
		email = self.cleaned_data.get("email")
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError('Email Address is already taken')
		return email


	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")
		if password2 != password:
			raise forms.ValidationError("Password must match")
		return data