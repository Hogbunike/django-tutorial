from django import forms
from django.forms import ModelForm
from .models import Venue

# create a venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'phone')
