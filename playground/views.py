from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem

def say_hello(request):
    queryset = TaggedItem.objects.ge_tags_for(Product, 1)
    return render(request, 'hello.html', {'name':'John Doe', 'tags':list(queryset)})