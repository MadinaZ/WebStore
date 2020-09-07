from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

#whenever there is a request to the products call this index function
#we need map this URL to this function
#URL - Uniform Resource Locator(Address)

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})#use this function to render a template
# Create your views here.


def new(request): #every view function should take http request
    return HttpResponse("New Products")
