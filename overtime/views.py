from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import AddOvertime, AddOvertimeType
from .models import Overtime
from contacts.forms import AddBranch
from .filters import OvertimeFilter

# Create your views here.

def overtimeindex(request):
    overtime_lst = Overtime.objects.select_related('overtime_type').filter(overtime_user=str(request.user))
    overtime_dckt = {'overtime':overtime_lst}

    overtime_filter = OvertimeFilter(request.GET, queryset=overtime_lst)
    overtime_dckt['filter'] = overtime_filter

    form = AddOvertime()
    overtime_dckt['form'] = form

    BForm = AddBranch()
    overtime_dckt['BForm'] = BForm

    OTForm = AddOvertimeType()
    overtime_dckt['OTForm'] = OTForm

    if request.method == 'POST':
        form = AddOvertime(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            print(str(obj.overtime_date_begin))
            obj.overtime_user = str(request.user)
            obj = form.save()

            return redirect('/nadgodziny')

        else:
            print("AddOvertime form isn't valid")
            form = AddBranch(request.POST)

            if form.is_valid():
                obj = form.save(commit=False)
                obj = form.save()
                return redirect('/nadgodziny')

            else:
                form = AddOvertimeType(request.POST)

                if form.is_valid():
                    obj = form.save()
                    return redirect('/nadgodziny')

    return render(request, 'overtimes/overtimes.html', context = overtime_dckt)