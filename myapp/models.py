from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=200,null=True,blank=True)
    username = models.CharField(max_length=200,null=True,blank=True)
    secret_id = models.CharField(max_length=200,null=True,blank=True)
    
    def __str__(self):
        return self.name 
    
class SecretData(models.Model):
    uid = models.CharField(max_length=200)
    key = models.CharField(max_length=200,null=True,blank=True)
    value = models.CharField(max_length=200,null=True,blank=True)
    
    def __str__(self):
        return self.uid 
    
