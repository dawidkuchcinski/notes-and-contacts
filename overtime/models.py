from django.db import models
from contacts import models as contacts_models

# Create your models here.

class Overtime_type(models.Model):
    overtime_type_name = models.CharField(max_length=50)
    overtime_hour_cost = models.IntegerField()

    def __str__(self):
        return self.overtime_type_name
    

class Overtime(models.Model):
    overtime_type = models.ForeignKey(Overtime_type, on_delete=models.CASCADE)
    overtime_branch = models.ForeignKey(contacts_models.Branch, on_delete=models.CASCADE)
    overtime_date_begin = models.DateTimeField()
    overtime_date_end = models.DateTimeField()
    overtime_user = models.CharField(max_length=50, null=True)

    class Meta:
        ordering = ['overtime_date_begin']
    
    def __str__(self):
        overtime_start = str(self.overtime_date_begin)
        return self.overtime_branch.branch_shortcut + " " + overtime_start
