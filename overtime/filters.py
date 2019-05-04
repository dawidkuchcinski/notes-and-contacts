from .models import Overtime
import django_filters

class OvertimeFilter(django_filters.FilterSet):
    class Meta:
        model = Overtime
        fields = {
            'overtime_date_begin': ['gt',], 
            'overtime_date_end': ['lt',],
        }