from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index(request):
    return render (request, 'Club/index.html')

def members(request):
    members_list = Meeting.objects.all()
    return render(request, 'Club/members.html', {'members_list': members_list})
