from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Events
from .forms import VenueForm

def add_venue(request):
    form = VenueForm
    return render(request, 'events/add_venue.html', {'form':form})


def all_events(request):
    event_list = Events.objects.all()
    return render(request, 'events/events_list.html', {'event_list': event_list})

def home(request, year=datetime.now().year, month=datetime.now().strftime("%B")):
    name = "Henry"
    month = month.title()
    month_num = list(calendar.month_name).index(month)
    month_num = int(month_num)

    cal = HTMLCalendar().formatmonth(year, month_num)
    return render(request, "events/home.html", {
        "name": name,
        "age": 26,
        "year": year,
        "month": month,
        "month_num": month_num,
        "cal": cal
    })
