from django import forms
from overtime.models import Overtime, Overtime_type

class AddOvertime(forms.ModelForm):
    class Meta:
        model = Overtime
        overtime_date_begin = forms.DateField(widget=forms.DateInput(format = '%Y-%m-%d %H:%M:%S'), 
                                 input_formats=('%Y-%m-%d %H:%M:%S',))
        overtime_date_end = forms.DateField(widget=forms.DateInput(format = '%Y-%m-%d %H:%M:%S'), 
                                 input_formats=('%Y-%m-%d %H:%M:%S',))
        widgets = {'overtime_date_begin': forms.DateInput(attrs={'class': 'datepicker'}), 'overtime_date_end': forms.DateInput(attrs={'class': 'datepicker'})}
        exclude = ['overtime_user']


class AddOvertimeType(forms.ModelForm):
    class Meta:
        model = Overtime_type
        fields = '__all__'