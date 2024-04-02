from django.contrib import admin

# Register your models here.

from .models import Event, Topic, Message, User

admin.site.register(User)
admin.site.register(Event)
admin.site.register(Topic)
admin.site.register(Message)

