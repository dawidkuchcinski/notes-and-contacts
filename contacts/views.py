from django.shortcuts import render, redirect
from .models import Contact
from .forms import AddContact, AddBranch

# Create your views here.

def contactindex(request):
    contact_lst = Contact.objects.order_by('last_name', 'first_name')
    contact_dckt = {'contact':contact_lst}

    form = AddContact()
    contact_dckt['form'] = form

    BForm = AddBranch()
    contact_dckt['BForm'] = BForm

    if request.method == 'POST':
        form = AddContact(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.company_name = str(request.user.groups.all()[0].name)
            obj = form.save()
            return redirect('/kontakty')

        else:
            form = AddBranch(request.POST)
                
            if form.is_valid():
                obj = form.save(commit=False)
                obj = form.save()
                return redirect('/kontakty')
    

    return render(request, 'contacts/contacts.html', context=contact_dckt)