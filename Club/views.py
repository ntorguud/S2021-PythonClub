from django.shortcuts import render
from .models import Meeting, MeetingMinute, Resource, Event
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render (request, 'Club/index.html')

def members(request):
    members_list = User.objects.all()
    return render(request, 'Club/members.html', {'members_list': members_list})

def resource(request):
    resource_list = Resource.objects.all()
    return render(request, 'Club/resource.html', {'resource_list': resource_list})

