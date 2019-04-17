from django.shortcuts import render
from contacts.models import Branch
from contacts.forms import AddBranch

# Create your views here.

def branchsindex(request):
    branch_lst = Branch.objects.order_by('branch_city')
    branch_dckt = {'branch':branch_lst}
    
    BForm = AddBranch()
    branch_dckt['BForm'] = BForm

    if request.method == 'POST':
        form = AddBranch(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj = form.save()
            return redirect('/placowki')

    return render(request, 'branchs/branchs.html', context=branch_dckt)