from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse , JsonResponse
from django.shortcuts import render , redirect
from .forms import ContactForm


def Home_Page(request):
	#print(request.session.get('user','Unknown'))
	context = {
		'title': 'Home Page ',
		'user' : request.user,
		'content':'This is the content of home page',
		#'premium_content' : 'Yehhhhhhhhh Upper'
	}
	if request.user.is_authenticated:
		context["premium_content"] = "Yehhhhhhhhh Lower"
	else:
		context["premium_content"] = None
	return render(request,'home_page.html',context)

def About_Page(request):
	context = {
		'title': 'About Page',
		'content':'This is the content of About page'
	}
	return render(request,'home_page.html',context)

def Contact_Page(request):
	contact_form = ContactForm(request.POST or None)

	context = {
		'title': 'Contact Page',
		'content':'This is the content of Contact page',
		'form': contact_form
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
		if request.is_ajax():
			return JsonResponse({'message':'Thank you for your Submission'})
	if contact_form.errors:
		errors = contact_form.errors.as_json()
		if request.is_ajax():
			return HttpResponse(errors, status=400, content_type = 'application/json')
	# if request.method == 'POST':
	# 	print (request.POST.get('fullname'))
	# 	print (request.POST.get('email'))
	# 	print (request.POST.get('message'))
	return render(request,'contact/contact.html',context)
