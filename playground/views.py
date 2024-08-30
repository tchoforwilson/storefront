from django.shortcuts import render
from django.db import connection
from store.models import Order, OrderItem, Product, Customer, Collection

def say_hello(request):
    
    with connection.cursor() as cursor:
    
        cursor.callproc('get_customers', [1, 2, 3, 'a'])
    
    
    return render(request, 'hello.html', {'name':'John Doe', 'result':list(queryset)})