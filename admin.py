from django.contrib import admin
from .models import Venue
from .models import Events
from .models import MyClubUsers

admin.site.register(Venue)
admin.site.register(Events)
admin.site.register(MyClubUsers)