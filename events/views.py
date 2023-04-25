from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Events, Venue
from .forms import VenueForm, EventForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import csv
# imports for pdf
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# imports for pagination
from django.core.paginator import Paginator


# Generate a PDF file venue list
def venue_pdf(request):
    #     Create a bytestream buffer
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # create a text object
    textob =c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    # designate the model
    venues = Venue.objects.all()
    lines = []
    #     Loop through
    for venue in venues:
        lines.append(venue.name)
        lines.append(venue.address)
        lines.append(venue.phone)
        lines.append(venue.email_address)
        lines.append(" ")
    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename="venue.pdf")


def venue_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=venues.csv'
    # create a csv writer
    writer = csv.writer(response)

    # Designate the model
    venues = Venue.objects.all()

    # add column headings to the csv file
    writer.writerow(['Venue Name', 'Address', 'Phone Number', 'Email Address'])

    # Loop Through venues and output
    for venue in venues:
       writer.writerow([venue.name, venue.address, venue.phone, venue.email_address])

    return response



# Generate Text file venue list
def venue_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=venues.txt'
    # Designate the model
    venues = Venue.objects.all()
    lines = []

    # Loop Through venues and output
    for venue in venues:
        lines.append(f'{venue.name}\n\n {venue.address}\n\n {venue.phone}\n\n {venue.email_address}\n\n')

    response.writelines(lines)
    return response

# delete a venue
def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('venue-list')
    return redirect('venue-list')


# delete an event
def delete_event(request, event_id):
    event = Events.objects.get(pk=event_id) 
    event.delete()
    return redirect('event_list')


def update_event(request, event_id):
    event = Events.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=Events)
    if form.is_valid():
        form.save()
        return redirect('event_list')
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
    # set up pagination
    p = Paginator(Venue.objects.all(), 2)
    page = request.GET.get('page')
    venues = p.get_page(page)
    nums = 'a' * venues.paginator.num_pages
    return render(request, 'events/venues.html', {'venues_list': venues_list, 'venues': venues, 'nums': nums})



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
    event_list = Events.objects.all().order_by('event_date')
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
