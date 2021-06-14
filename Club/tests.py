from Club.views import newMeeting
from django.test import TestCase
from .models import User
from .models import Meeting, MeetingMinute, Resource, Event
import datetime, time
from .forms import MeetingForm
from django.urls import reverse_lazy, reverse

# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.type=Meeting(typename='Discord Server')
        self.user=User(username='Tuul')
        self.meeting=Meeting(meetingtitle='Python Club Discord Server', meetingdate=datetime('6/07/2021'), meetingtime=time('12.00pm'), location='Seattle, WA', agenda='meet up')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Python Club Discord Server')

    def test_tablename(self):
        self.assertEqual(str(Meeting.meta.db_table), 'meeting')

class MeetingMinuteTest(TestCase):
    def setUp(self):
        self.type=MeetingMinute(typename='meetingminutes')
        self.user=User(username='Jenny')
        self.meetingminute=MeetingMinute(meetingid='01', attendance='voluntary', minutestext='Welcome')
    
class ResourceTest(TestCase):
    def setUp(self):
        self.type=Resource(typename='resources')
        self.user=User(userid='Jack')
        self.resource=Resource(resourcename='Python.org Community', resourcetype='url', resourceurl='https://www.python.org/community/', dateentered=datetime('06/07/2021'), description='support')

class NewMeetingForm(TestCase):
    #valid form data
    def test_MeetingForm(self):
        data={
                'meetingtitle': 'Coding Club: Learn Python', 
                'meetingdate': '6/08/2021', 
                'user': 'Naran', 
                'meetingtime': '12.00pm', 
                'location': 'https://www.youtube.com/watch?v=8leDF7AADMo',
                'agenda': 'Welcome new members, Club website'
        }
        form=MeetingForm(data)
        self.assertTrue(form.is_valid)

    def test_MeetingForm_Invalid(self):
        data={
                'meetingtitle': 'Coding Club: Learn Python', 
                'meetingdate': 'June/08/2021', 
                'user': 'Naran', 
                'meetingtime': '12.00pm', 
                'location': 'https://www.youtube.com/watch?v=8leDF7AADMo',
                'agenda': 'Welcome new members, Club website'
        }
        form=MeetingForm(data)
        self.assertFalse(form.is_valid)

class New_Meeting_Authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testTuul', password='Mongolia@123')
        self.type=Meeting.objects.create(typename='Discord Server')
        self.meeting=Meeting.objects.create(meetingtitle='Python Club Discord Server', meetingdate=datetime('6/07/2021'), meetingtime=time('12.00pm'), location='Seattle, WA', agenda='meet up', user=self.test_user)

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newmeeting'))
        self.assertRedirects(response, '/accounts/login/?next=/Club/newmeeting/')

