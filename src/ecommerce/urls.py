"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.views import LogoutView
from addresses.views import checkout_address_create_view , checkout_address_reuse_view
from accounts.views import Register_Page, Login_Page , guest_register_view
from .views import Home_Page, About_Page, Contact_Page
from carts.views import cart_detail_api_view

urlpatterns = [
	path('', Home_Page, name='home'),
	path('about/', About_Page, name='about'),
	path('contact/', Contact_Page, name='contact'),
    path('register/', Register_Page, name = 'register'),
    path('register/guest/', guest_register_view, name = 'guest_register'),
    path('login/', Login_Page, name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('checkout/address/create/', checkout_address_create_view, name = 'checkout_address_create'),
    path('checkout/address/reuse/', checkout_address_reuse_view, name = 'checkout_address_reuse'),
    #path('cart/', cart_home , name='cart'),
    path('admin/', admin.site.urls),

    path('api/cart/', cart_detail_api_view, name = 'cart_api'),

    path('cart/', include("carts.urls", namespace='cart')),
    path('products/', include("products.urls", namespace='products')),
    path('search/', include("search.urls", namespace='search'))

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)