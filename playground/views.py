from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product, OrderItem

def say_hello(request):
    products = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct())
    return render(request, 'hello.html', {'name':'John Doe', 'products':products})