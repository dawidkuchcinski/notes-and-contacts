from django.shortcuts import render
from .models import Note
from .forms import AddNote

# Create your views here.

def notesindex(request):
    note_lst = Note.objects.order_by('-modify_time').select_related('contacts')
    note_dckt = {'note':note_lst}

    form = AddNote()
    note_dckt['form'] = form

    if request.method == 'POST':
        form = AddNote(request.POST)

        if form.is_valid():
            obj = form.save()
            return redirect('/notatki')

    return render(request, 'notes/notes.html', context=note_dckt)
