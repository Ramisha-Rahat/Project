from django.db import models

# Create your models here.

class saveContact(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    subject= models.CharField(max_length=100)
    message= models.TextField()
