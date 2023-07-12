from django import forms
from django.forms import ModelForm
from .models import Venue, Events
# Admin Super User EventForm
class AdminEventForm(ModelForm):
    class Meta:
        model = Events
        fields = ('name', 'event_date', 'venue', 'manager', 'attendees', 'description')
        labels = {
            'name': "",
            'event_date': "YYYY-MM-DD HH:MM",
            'venue': "Venue",
            'manager': 'Manager',
            'attendees': 'Attendees',
            'description': '',
            }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Event Name'}),
            'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Event date'}),
            'venue': forms.Select(attrs={'class':'form-select', 'placeholder': 'Venue'}),
            'manager': forms.Select(attrs={'class':'form-select', 'placeholder': 'Manager'}),
            'attendees': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder': 'Attendees'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }

# User Event Form
class EventForm(ModelForm):
    class Meta:
        model = Events
        fields = ('name', 'event_date', 'venue', 'attendees', 'description')
        labels = {
            'name': "",
            'event_date': "YYYY-MM-DD HH:MM",
            'venue': "Venue",
            'attendees': 'Attendees',
            'description': '',
            }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Event Name'}),
            'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Event date'}),
            'venue': forms.Select(attrs={'class':'form-select', 'placeholder': 'Venue'}),
            'attendees': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder': 'Attendees'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }


# create a venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'phone')
        labels = {
            'name': "",
            'address': "",
            'phone': "",
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Venue Name'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Venue Address'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Contact Phone'}),
        }
