from Club.models import Meeting
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('members/', views.members, name='members'),
    path('resource/', views.resource, name='resource'),
    path('meetingdetail/<int:id>', views.meetingDetail, name='detail')
]
