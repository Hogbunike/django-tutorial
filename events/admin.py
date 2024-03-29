from django.contrib import admin
from .models import Venue
from .models import Events
from .models import MyClubUsers
from django.contrib.auth.models import Group

# admin.site.register(Venue)
# admin.site.register(Events)
admin.site.register(MyClubUsers)

# Remove Groups
admin.site.unregister(Group)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address')

@admin.register(Events)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'event_date', 'description', 'manager', 'approved')
    list_display = ('name', 'event_date', 'venue')
    list_filter = ('event_date', 'venue')
    ordering = ('event_date',)