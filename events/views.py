from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Events, Venue
from .forms import VenueForm, EventForm
from django.http import HttpResponseRedirect

def update_event(request, event_id):
    event = Events.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=Events)
    if form.is_valid():
        form.save()
        return redirect('event-list')
    return render(request, 'events/update_event.html', {'event': event, 'form': form})


def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True


    return render(request, 'events/add_event.html', {'form':form, 'submitted': submitted})


def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('venue-list')
    return render(request, 'events/update_venue.html', {'venue': venue, 'form': form})

def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'events/search_venues.html', {'searched': searched, 'venues': venues})
    else:
        return render(request, 'events/search_venues.html', {})

def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'events/show_venue.html', {'venue': venue})

def all_venues(request):
    venues_list = Venue.objects.all()
    return render(request, 'events/venues.html', {'venues_list': venues_list})


def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True


    return render(request, 'events/add_venue.html', {'form':form, 'submitted': submitted})


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
