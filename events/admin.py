from django.contrib import admin

from .models import DateCollect, Event

# Register your models here.
admin.site.register(Event)
admin.site.register(DateCollect)
