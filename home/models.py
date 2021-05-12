from django.db import models

# Create your models here.
class Data(models.Model):
    Username=models.CharField(max_length=15)
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=100,default='')
    Password=models.CharField(max_length=20)
    SEOmail=models.CharField(max_length=100, default='')
    SEOpassword=models.CharField(max_length=20)
    seoip=models.CharField(max_length=20,default='')
    Counter=models.CharField(max_length=21,default='')