from django import forms
from contacts.models import Contact, Branch

class AddContact(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['company_name']

class AddBranch(forms.ModelForm):
    class Meta:
        model = Branch
        fields = '__all__'