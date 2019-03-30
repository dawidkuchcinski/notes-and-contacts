from django import forms
from notes.models import Note

class AddNote(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ['status', 'add_time', 'modify_time', 'user']