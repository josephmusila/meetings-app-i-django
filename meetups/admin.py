from django.contrib import admin
from .models import Meetup,Location,Participants

# Register your models here.


class MeetupAdmin(admin.ModelAdmin):
    list_display=("title","date","location",)
    list_filter=("location","date",)
    prepopulated_fields={"slug":("title",)}
    
    
class LocationAdmin(admin.ModelAdmin):
    list_display=("name",)
    
    
admin.site.register(Meetup,MeetupAdmin)

admin.site.register(Location,LocationAdmin)

admin.site.register(Participants)