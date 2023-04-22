from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:year>/<str:month>', views.home, name="home"),
    path('events', views.all_events, name="event_list"),
    path('add_venue', views.add_venue, name='add-venue'),
    path('list_venues', views.all_venues, name='venue-list'),
    path('show_venue/<int:venue_id>', views.show_venue, name='show-venue'),
    path('search_venues', views.search_venues, name='search_venues'),
    path('update_venue/<int:venue_id>', views.update_venue, name='update_venue'),
    path('add_event', views.add_event, name='add-event'),
<<<<<<< HEAD
    path('update_event/<event_id>', views.update_event, name='update-event'),
    path('delete_event/<int:event_id>', views.delete_event, name='delete-event'),
=======
    path('update_event/<int:event_id>', views.update_event, name='update-event'),
    path('delete_event/<int:event_id>', views.delete_event, name='delete-event'), 
    #You were passing the wrong parameter, instead of venue_id, you were passing event_id
>>>>>>> bf8b7c9c6e3cfeabad5e68785ea255abd35d7687
    path('delete_venue/<int:venue_id>', views.delete_venue, name='delete-venue'),
    path('venue_text', views.venue_text, name='venue_text'),
    path('venue_csv', views.venue_csv, name='venue_csv'),
    path('venue_pdf', views.venue_pdf, name='venue_pdf'),



]
