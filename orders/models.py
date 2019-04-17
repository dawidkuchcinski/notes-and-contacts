from django.db import models

# Create your models here.

class Email(models.Model):
    email_address = models.CharField(max_length=50)
    email_subject = models.CharField(max_length=100)

    class Meta:
        ordering = ['email_subject', 'email_address']
    
    def __str__(self):
        return self.email_subject + " " + self.email_address

class Item(models.Model):
    item_model = models.CharField(max_length=50)
    item_type = models.CharField(max_length=50)

    class Meta:
        ordering = ['item_type', 'item_model']
    
    def __str__(self):
        return self.item_type + " " + self.item_model

class Order(models.Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_quantity = models.IntegerField(null=False)
    order_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-order_time']

    def __str__(self):
        id2 = str(self.id)
        return id2
