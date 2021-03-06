from django.db import models

# Create your models here.
class Branch(models.Model):
    branch_shortcut = models.CharField(max_length=50)
    branch_phone_number = models.CharField(max_length=15)
    branch_email_address = models.EmailField(max_length=254)
    branch_city = models.CharField(max_length=50)
    branch_street = models.CharField(max_length=50)
    branch_safo_number = models.IntegerField(null=True)
    branch_svp_id = models.IntegerField(null=True)

    class Meta:
        ordering = ['branch_shortcut']

    def __str__(self):
        return self.branch_city
    

class Contact(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=15)
    email_address = models.EmailField(max_length=254)
    company_name = models.CharField(max_length=50)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return self.last_name + " " + self.first_name + " Nr: " + self.phone_number
    
