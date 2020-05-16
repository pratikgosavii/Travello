from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User
from travello.models import Destination

# Create your models here.
class clientdetails(models.Model):
    first_name=models.CharField(max_length=50,default='vdx')
    middle_name=models.CharField(max_length=50,default='vdx')
    last_name=models.CharField(max_length=50,default='vdx')
    gmail=models.EmailField(max_length=50, default='gsh')
    code=models.CharField(max_length=50, default='gsh')
    phone=models.CharField(default=1,max_length=50)
    occupation=models.CharField(max_length=50,default='vdx')
    status=models.CharField(max_length=50,default='vdx')
    people_mens=models.IntegerField(default=1)
    people_female=models.IntegerField(default=1)
    people_childern=models.IntegerField(default=1)
    any_message=models.CharField(max_length=50,default='vdx')
    address_line1=models.CharField(max_length=50,default='vdx')
    address_line2=models.CharField(max_length=50,default='vdx')
    zip1=models.IntegerField(default=1)
    city=models.CharField(max_length=50,default='vdx')
    state=models.CharField(max_length=50,default='vdx')
    country=models.CharField(max_length=50,default='vdx')
    Date_From = models.CharField(max_length=50, default= datetime.now)
    Date_To = models.CharField(max_length=50, default= datetime.now)
    mode=models.CharField(default="not define", max_length=50)
    additionalinformation=models.CharField(max_length=50,default='vdx')
    city_name = models.CharField(max_length=50,default='vdx')
    price = models.IntegerField(default=5654)
    dec = models.TextField(default='hdhfzsds')
    image = models.ImageField(upload_to='pics',default='picc')
    agentnumber = models.CharField(default="8237377298", max_length=10)
    agent_address=models.CharField(default="not define", max_length=50)
    
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.first_name


