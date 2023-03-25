from django.db import models

class MyClubUsers(models.Model):
    first_name = models.CharField('First Name', max_length=30)
    last_name = models.CharField('Last Name', max_length=30)
    email_address = models.EmailField('Email', max_length=25)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Venue(models.Model):
    name = models.CharField('Venue name', max_length=120)
    address = models.CharField('Address', max_length=120)
    phone = models.IntegerField('Contact Phone',max_length=15)
    email_address = models.EmailField('Email Address', max_length=25)

    def __str__(self):
        return self.name

class Events(models.Model):
    name = models.CharField('Event name', max_length=120)
    event_date = models.DateTimeField('Event date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    # venue = models.CharField(max_length=120)
    manager = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUsers, blank=True)

    def __str__(self):
        return self.name