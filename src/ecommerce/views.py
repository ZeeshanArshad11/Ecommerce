from django.http import HttpResponse
from django.shortcuts import render


def Home_Page(request):
	context = {
		'title': 'Home Page',
		'content':'This is the content of home page'
	}
	return render(request,'home_page.html',context)

def About_Page(request):
	context = {
		'title': 'About Page',
		'content':'This is the content of About page'
	}
	return render(request,'home_page.html',context)

def Contact_Page(request):
	context = {
		'title': 'Contact Page',
		'content':'This is the content of Contact page'
	}
	return render(request,'home_page.html',context)