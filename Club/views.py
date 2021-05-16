from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index(request):
    return render (request, 'Club/index.html')

def products(request):
    product_list = Product.objects.all()
    return render(request, 'Club/products.html', {'product_list': product_list})
