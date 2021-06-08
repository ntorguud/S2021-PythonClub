from django import forms
from .models import Meeting, MeetingMinute, Resource, Event
from django.contrib.auth.models import User

class MeetingForm(forms.ModelForm):
    class Meta:
        model=Meeting
        fields='__all__'