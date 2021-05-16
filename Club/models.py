from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meeting(models.Model):
    meetingtitle = models.CharField(max_length=255)
    meetingdate = models.DateField()
    meetingtime = models.DateTimeField()
    location = models.TextField(null=True, blank=True)
    agenda = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table = 'Meeting'

class MeetingMinutes(models.Model):
    meetingid = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    attendance = models.ManyToManyField(User, blank=True)
    minutestext = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.meetingid

        class Meta:
            db_table = 'MeetingMinutes'

class Resource(models.Model):
    resourcename = models.CharField(max_length=255)
    resourcetype = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    resourceurl = models.URLField()
    dateentered = models.DateField()
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table = 'Resource'

class Event(models.Model):
    eventtitle = models.CharField(max_length=255)
    location = models.TextField(null=True,blank=True)
    eventdate = models.DateField()
    eventtime = models.DateTimeField()
    description = models.TextField()
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
