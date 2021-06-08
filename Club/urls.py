from Club.models import Meeting, MeetingMinute, Resource, Event
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('members/', views.members, name='members'),
    path('resource/', views.resource, name='resource'),
    path('meeting/', views.meeting, name='meeting'),
    path('meetingDetail/<int:id>', views.meetingDetail, name='meetingdetail'),
    path('newmeeting/', views.newMeeting, name='newmeeting'),
]
