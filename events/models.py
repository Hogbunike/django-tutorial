from django.db import models
from django.contrib.auth.models import User
from datetime import date

class MyClubUsers(models.Model):
    first_name = models.CharField('First Name', max_length=30)
    last_name = models.CharField('Last Name', max_length=30)
    email_address = models.EmailField('Email', max_length=25)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Venue(models.Model):
    name = models.CharField('Venue name', max_length=100)
    address = models.CharField('Address', max_length=150,)
    phone = models.IntegerField('Contact Phone', max_length=15)
    email_address = models.EmailField('Email Address', max_length=25)
    owner = models.IntegerField('Venue Owner', blank=False, default=1)
    venue_img = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name

class Events(models.Model):
    name = models.CharField('Event name', max_length=100)
    event_date = models.DateTimeField('Event date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    # venue = models.CharField(max_length=120)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUsers, blank=True)
    approved = models.BooleanField('Approved', default=False)

    def __str__(self):
        return self.name
    
    @property
    def Days_till(self):
        today = date.today()
        days_till = self.event_date.date() - today
        days_till_stripped = str(days_till).split(",",1)[0]
        return days_till_stripped
    
    @property
    def Is_Valid(self):
        today = date.today()
        if self.event_date.date() < today:
            event = "Past"
        else:
            event = "Still Valid"
        return event