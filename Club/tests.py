from django.test import TestCase
from .models import User
from .models import Meeting, MeetingMinute, Resource, Event
import datetime, time

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
    
class ResourceTest(TestCase):
    def setUp(self):
        self.type=Resource(typename='resources')
        self.user=User(userid='Jack')
        self.resource=Resource(resourcename='Python.org Community', resourcetype='url', resourceurl='https://www.python.org/community/', dateentered=datetime('06/07/2021'), description='support')