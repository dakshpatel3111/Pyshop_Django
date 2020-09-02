from django.http import HttpResponse
from django.shortcuts import render
from .models import Product,Offers


def index(request):
    products = Product.objects.all()
    return render(request , 'index.html', {'products':products})



def cart(request):
    return render(request , 'cart.html', {'cart':cart})

# This is  the request for products/news in the url