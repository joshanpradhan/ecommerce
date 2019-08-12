from django.db.models import Q
from django.shortcuts import render
from products.models import Product
from django.views.generic import ListView
from carts.models import Cart

# Create your views here.


class SearchProductView(ListView):
    template_name = "search/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(
            *args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q', None)
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.featured()
