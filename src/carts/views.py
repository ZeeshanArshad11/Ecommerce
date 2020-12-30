from django.shortcuts import render, redirect
from django.http import JsonResponse

from accounts.forms import LoginForm, GuestForm
from addresses.forms import AddressForm

from accounts.models import GuestEmail
from products.models import Product
from .models import Cart
from orders.models import Order
from billing.models import BillingProfile
from addresses.models import Address

# Create your views here.

# def cart_create(user=None):
# 	cart_obj = Cart.objects.create(user=None)
# 	print('New Cart ID Created')
# 	return cart_obj

def cart_detail_api_view(request):
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	products =[ {
		"id":x.id,
		"url":x.get_absolute_url(),
		"name":x.name ,
		"price":x.price
	} 
	for x in cart_obj.products.all()] # one Line Code
	# products_list = [] #  Extended method
	# for x in cart_obj.products.all():
	# 	products_list.append(
	# 		{
	# 		"products": products,
	# 		"subtotal": cart_obj.subtotal,
	# 		"total":cart_obj.total
	# 		})
	cart_data = {"products": products, "subtotal": cart_obj.subtotal, "total":cart_obj.total}
	return JsonResponse(cart_data)

def cart_home(request):
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	# cart_id = request.session.get("cart_id" , None)
	# qs = Cart.objects.filter(id = cart_id)
	# if qs.count() == 1:
	# 	cart_obj = qs.first()
	# 	if request.user.is_authenticated and cart_obj.user is None:
	# 		cart_obj.user = request.user
	# 		cart_obj.save()
	# else:
	# 	cart_obj = Cart.objects.new(user = request.user)
	# 	request.session['cart_id'] = cart_obj.id
	#print(request.session)
	#print(request.session.session_key)
	#request.session.set_expiry(300) # 5 Minutes
	#request.session['user'] = request.user.username
	return render(request, "carts/home.html",{'cart': cart_obj})


def cart_update(request):
	product_id = request.POST.get('product_id')

	if product_id is not None:
		try:
			product_obj = Product.objects.get(id = product_id)
		except Product.DoesNotExist:
			print("Message to the User , Product is gone?")
			return redirect("cart:home")
		cart_obj, new_obj = Cart.objects.new_or_get(request)
		if product_obj in cart_obj.products.all():
			cart_obj.products.remove(product_obj)
			added = False
		else:
			cart_obj.products.add(product_obj)
			added = True

	request.session['cart_item'] = cart_obj.products.count() # display Total cart item in nav bar  

	#return redirect(product_obj.get_absolute_url())
	if request.is_ajax():
		# print("ajax Response")
		json_data = {
		"added": added,
		"removed" : not added,
		"cartItemCount" : cart_obj.products.count(),
		}
		return JsonResponse(json_data)
	return redirect("cart:home")


def checkout_home(request):
	cart_obj, cart_created = Cart.objects.new_or_get(request)
	order_obj = None
	if cart_created or cart_obj.products.count() == 0:
		return redirect("cart:home")
	
	login_form 	= LoginForm()
	guest_form 	= GuestForm()
	address_form = AddressForm()
	billing_address_id = request.session.get("billing_address_id", None)
	shipping_address_id = request.session.get("shipping_address_id", None)
	

	billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
	address_qs = None
	if billing_profile is not None:
		if request.user.is_authenticated:
				address_qs = Address.objects.filter(billing_profile = billing_profile)
				# shipping_address_qs 	= address_qs.filter(address_type = 'shipping')
				# billing_address_qs 		= address_qs.filter(address_type = 'billing')

		order_obj , order_obj_created = Order.objects.new_or_get(billing_profile , cart_obj )
		request.session['order_id'] = order_obj.order_id
		if shipping_address_id:
			order_obj.shipping_address = Address.objects.get(id=shipping_address_id)
			del request.session['shipping_address_id']
		if billing_address_id:
			order_obj.billing_address = Address.objects.get(id=billing_address_id)
			del request.session['billing_address_id']
		if shipping_address_id or billing_address_id:
			order_obj.save()

	if request.method == 'POST':
		#"Do some checks Here"
		is_done = order_obj.check_done()
		if is_done:
			order_obj.mark_paid()
			del request.session['cart_id']
			del request.session['cart_item']

			return redirect("cart:success")


	context = {
	"object" : order_obj,
	"billing_profile" : billing_profile,
	"login_form" : login_form,
	"guest_form" : guest_form,
	"address_form" : address_form,
	"address_qs" : address_qs
	}

	return render(request, "carts/checkout.html", context)


def checkout_done_view(request):
	order_id = request.session.get('order_id')
	try:
		order_obj = Order.objects.get(order_id=order_id)
	except DoesNotExist:
		print("Order doesn't exist.")
		
	context = {
		"object": order_obj
	}
	return render(request, 'carts/checkout_done.html', context)