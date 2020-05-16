from django.db import models


# Create your models here.




class Destination(models.Model):
    
    name = models.CharField(max_length=50,default='vdx')
    price = models.IntegerField(default=5654)
    dec = models.TextField(default='hdhfzsds')
    image = models.ImageField(upload_to='pics',default='picc')
    offer = models.BooleanField(default=False)
    agentnumber = models.CharField(default="8237377298", max_length=10)
    agent_address=models.CharField(default="not define", max_length=50)

    
    
   