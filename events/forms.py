from django import forms
from django.forms import ModelForm
from .models import Venue

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
