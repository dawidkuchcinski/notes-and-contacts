from django import forms
from contacts.models import Contact

class AddContact(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['company_name']