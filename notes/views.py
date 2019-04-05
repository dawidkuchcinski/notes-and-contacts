from django.shortcuts import render, redirect
from .models import Note
from .forms import AddNote

# Create your views here.

def notesindex(request):
    note_lst = Note.objects.select_related('contacts').filter(user=str(request.user)).order_by('status', '-modify_time')
    note_dckt = {'note':note_lst}

    form = AddNote()
    note_dckt['form'] = form

    if request.method == 'POST':
        form = AddNote(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.status_id = 1
            obj.user = str(request.user)
            obj = form.save()
            return redirect('/notatki')

    return render(request, 'notes/notes.html', context=note_dckt)
