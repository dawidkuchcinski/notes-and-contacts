from django import forms
from notes.models import Note

class AddNote(forms.ModelForm):
    class Meta:
        model = Note
        widgets = {
          'note_content': forms.Textarea(attrs={'rows':4, 'cols':15}),
        }
        exclude = ['status', 'add_time', 'modify_time', 'user']