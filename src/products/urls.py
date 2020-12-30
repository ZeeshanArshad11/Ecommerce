
from django.urls import path

from .views import (
    ProductListView, 
    #product_list_view, 
    #ProductDetailView, 
    #product_detail_view,
    #ProductFeaturedListView,
    #ProductFeaturedDetailView,
    ProductDetailSlugView
    )

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),  # URL against Class Based View (ListView)
    #path('featured/', ProductFeaturedListView.as_view(), name='featured'),  # URL against Class Based View (ListView) for Featured Product
    #path('products-pvc/', product_list_view, name='products-pvc'),  # URL against function based views
    #path('products/<pk>/', ProductDetailView.as_view(), name='products-detail'),  # URL against Class Based View (DetailView)
    path('<slug>/', ProductDetailSlugView.as_view(), name='detail'),  # URL against Class Based View (DetailView) for slug
    #path('featured/<pk>/', ProductFeaturedDetailView.as_view(), name='featured-detail'),  # URL against Class Based View (DetailView) for Featured Product
    #path('products-pvc/<pk>/', product_detail_view, name='products-pvc-detail'),  # URL against function based views
]
