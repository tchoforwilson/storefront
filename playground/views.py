from django.shortcuts import render
from store.models import Order, OrderItem, Product, Customer

def say_hello(request):
    queryset = Product.objects.all()
    queryset[0]
    list(queryset)
    return render(request, 'hello.html', {'name':'John Doe', 'tags':list(queryset)})