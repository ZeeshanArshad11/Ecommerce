#from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from products.models import Product

# Create your views here.
class SearchListView(ListView):
	template_name = "search/view.html"

	def get_context_data(self, *args, **kwargs):
		context = super(SearchListView, self).get_context_data(*args, **kwargs)
		#print(context)
		context['query'] = self.request.GET.get('q')
		return context

	def get_queryset(self, *args, **kwargs):
		request = self.request
		#print(request.GET)
		query = request.GET.get('q', None)
		#print(query)
		if query is not None:
			#lookups = Q(title__icontains=query) | Q(description__icontains=query) | Q(price__icontains=query)
			#return Product.objects.filter(lookups).distinct()
			#return Product.objects.filter(title__icontains=query)
			return Product.objects.search(query)
		#return Product.objects.all()
		return Product.objects.featured()