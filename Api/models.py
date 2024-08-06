from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    phone_no = models.CharField(max_length=12, unique=True)
    email = models.EmailField(blank=True, null=True) 
    # contact no is should be unique and email is not compalsoury 

class Contact(models.Model):
    user = models.ForeignKey(CustomUser, related_name='contacts', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    nickname =models.CharField(max_length=50)
    def __str__(self):
        return f'{self.name} ({self.phone_no})'
    
class Spam(models.Model):
    phone_no = models.CharField(max_length=12, unique=True)
    is_spam = models.BooleanField(default=True) 
    spam_count = models.IntegerField(default=0)
    #intially declear every no is not spam before marking CustomUser of our app 
    def __str__(self):
        return f'Spam report for {self.phone_no} by {self.reported_by.phone_no}'
   # Now this fun will show who mark spam to other users 