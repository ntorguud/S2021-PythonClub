from django.shortcuts import render
from .models import Product, ClubType, Review

# Create your views here.
def index(request):
    return render (request, 'Club/index.html')

def products(request):
    product_list = Product.objects.all()
    return render(request, 'Club/products.html', {'products_list': product_list})
