from django.contrib import admin
from notes.models import Note, Status

admin.site.register(Note)
admin.site.register(Status)