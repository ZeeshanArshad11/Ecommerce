from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

from accounts.models import GuestEmail
User = settings.AUTH_USER_MODEL

# emailid = 10000000 billing Profile
# user = 1 billing profile



class BillingProfileManager(models.Manager):
	def new_or_get(self, request):
		user = request.user
		obj = None
		created = False
		guest_email_id = request.session.get('guest_email_id')
		if user.is_authenticated:
			# logged in User Checkout ; Remember Payments Stuff
			obj , created = self.model.objects.get_or_create(user=user, email=user.email)
		elif guest_email_id is not None:
			# Guest User Checkout ; Auto Reload Payments Stuff
			guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
			obj , created = self.model.objects.get_or_create(email=guest_email_obj.email)
		else:
			pass

		created = True
		return obj , created

# Create your models here.

class BillingProfile(models.Model):
	user 		= models.OneToOneField(User, on_delete = None, null=True, blank=True)
	email 		= models.EmailField()
	active 		= models.BooleanField(default = True)
	update 		= models.DateTimeField(auto_now = True)
	timestamp 	= models.DateTimeField(auto_now_add = True)
	# customer_id in Stripe / Braintree

	objects = BillingProfileManager()


	def __str__(self):
		return self.email


# def billing_profile_created_receiver(sender, instance, created, *args, **kwargs):
# 	if created:
# 		print("Actual API request to Stripe/Braintree")
# 		instance.customer_id = new_id
# 		instance.save()



def user_created_receiver(sender, instance, created , *args, **kwargs):
	if created and instance.email:
		BillingProfile.objects.get_or_create(user=instance , email=instance.email)


post_save.connect(user_created_receiver , sender = User)
