from django import forms
from django.forms import ModelForm
from .models import Venue, Events

class EventForm(ModelForm):
    class Meta:
        model = Events
        fields = ('name', 'event_date', 'venue', 'manager', 'description', 'attendees')
        labels = {
            'name': "",
            'address': "",
            'phone': "",
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Event Name'}),
            'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Event date'}),
            'venue': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Venue'}),
            'manager': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Manager'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Description'})
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
