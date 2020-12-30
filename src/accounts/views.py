from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.utils.http import is_safe_url
from django.shortcuts import render , redirect




from .forms import LoginForm, RegisterForm, GuestForm
from .models import GuestEmail
# Create your views here.

def guest_register_view(request):
	guest_form = GuestForm(request.POST or None)
	context = {
		'title' : 'Guest Register Page',
		'content' : 'This is content of Guest Register Page',
		'form' : guest_form
	}
	next_ = request.GET.get('next')
	next_post = request.POST.get('next')
	redirect_path = next_ or next_post or None
	if guest_form.is_valid():
		email = guest_form.cleaned_data.get("email")
		new_guest_email = GuestEmail.objects.create(email=email)
		request.session['guest_email_id'] = new_guest_email.id
		#print(guest_form.cleaned_data)
		# Redirect to a success page.
		if is_safe_url(redirect_path, request.get_host()):
			return redirect(redirect_path)	# redirect to the exact path where user leaved
		else:
			return redirect("/register/") 		# redirect to register  
		
	return redirect("/register/") 


def Login_Page(request):
	login_form = LoginForm(request.POST or None)
	context = {
		'title' : 'Login Page',
		'content' : 'This is content of login Page',
		'form' : login_form
	}
	next_ = request.GET.get('next')
	next_post = request.POST.get('next')
	redirect_path = next_ or next_post or None
	if login_form.is_valid():
		#print(login_form.cleaned_data)
		#print(request.user.is_authenticated)
		username = login_form.cleaned_data.get("username")
		password = login_form.cleaned_data.get("password")
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			try:
				del request.session['guest_email_id']
			except:
				pass
				
			# Redirect to a success page.
			if is_safe_url(redirect_path, request.get_host()):
				return redirect(redirect_path)	# redirect to the exact path where user leaved
			else:
				return redirect("/") 		# redirect to Home Page 
		else:
			# Return an 'invalid login' error message.
			print('Error')

	return render(request, "accounts/login.html", context)


User = get_user_model()
def Register_Page(request):
	register_form = RegisterForm(request.POST or None)
	context = {
		'title' : 'Register Page',
		'content' : 'This is content of Register Page',
		'form' : register_form
	}
	if register_form.is_valid():
		#print(register_form.cleaned_data)
		username = register_form.cleaned_data.get("username")
		email = register_form.cleaned_data.get("email")
		password = register_form.cleaned_data.get("password")
		new_user = User.objects.create_user(username, email, password)
		print(new_user)

	return render(request, "accounts/register.html", context)