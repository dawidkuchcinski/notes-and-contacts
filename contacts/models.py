from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Branch(models.Model):
    branch_shortcut = models.CharField(max_length=50)
    branch_phone_number = models.CharField(max_length=15)
    branch_email_address = models.EmailField(max_length=254)
    branch_city = models.CharField(max_length=50)
    branch_street = models.CharField(max_length=50)

    def __str__(self):
        return self.branch_shortcut
    

class Contact(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=15)
    email_address = models.EmailField(max_length=254)
    company_name = models.CharField(max_length=50)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name + " Nr: " + self.phone_number
    
