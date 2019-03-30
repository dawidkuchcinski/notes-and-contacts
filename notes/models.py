from django.db import models
from contacts import models as contacts_models

# Create your models here.
class Status(models.Model):
    status_name = models.CharField(max_length=50)
    priority = models.IntegerField(null=True)

    def __str__(self):
        return self.status_name
    

class Note(models.Model):
    title = models.CharField(max_length=254)
    note_content = models.TextField()
    tag = models.CharField(max_length=50)
    contacts = models.ForeignKey(contacts_models.Contact, on_delete=models.CASCADE, blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True, null=True)
    modify_time = models.DateTimeField(auto_now=True, null=True)
    user = models.CharField(max_length=50, default='bugs')

    def __str__(self):
        return self.title
    
    
