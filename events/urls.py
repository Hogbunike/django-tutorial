from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:year>/<str:month>', views.home, name="home"),
    path('events', views.all_events, name="event_list"),
    path('add_venue', views.add_venue, name='add-venue'),
    path('list_venues', views.all_venues, name='venue-list'),
    path('show_venue/<venue_id>', views.show_venue, name='show-venue'),


]
