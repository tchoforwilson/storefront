from django.shortcuts import render
from store.models import Order, OrderItem, Product, Customer, Collection

def say_hello(request):
    collection = Collection.objects.get(pk=11)
    collection.featured_product = None
    collection.save()
    
    return render(request, 'hello.html', {'name':'John Doe'})