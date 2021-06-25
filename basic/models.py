from django.db import models
from django.contrib.auth.models import User
from .CITY_LIST import CITY_LIST
import geocoder

mapbox_token = 'pk.eyJ1IjoiaW1sb3JkaW1wYWxlciIsImEiOiJja3Fhbm1pcnkwYWhpMnBrZGFraHc3NTRlIn0.YuUk6OD-kfnZqdCLrf2SVg'

class Paitent(models.Model):
    name = models.CharField(max_length=100 , null=True, blank=True)
    phone = models.CharField(max_length=10 , null=True, blank=True)
    email = models.EmailField(max_length=1000 , null=True , blank=True)
    age = models.CharField(max_length=100  , null=True, blank=True)
    user = models.OneToOneField(User , on_delete=models.CASCADE)

    #img 

    def __str__(self):
        return self.user.username



class Category(models.Model):
    name = models.CharField(max_length=1000)
    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100 , null=True, blank=True)
    age = models.IntegerField(default=1)
    address = models.TextField()
    city = models.CharField(max_length=100 , choices=CITY_LIST , null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    user = models.OneToOneField(User , on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)

    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address , key= mapbox_token)
        g = g.latlng
        self.lat = g[0]
        self.long = g[1]
        return super(Doctor , self).save(*args, **kwargs)
    def __str__(self):
        return str('Dr. ' + self.user.username)

STATUS_CHOICES = (
    ('inactive','inactive'),
    ('active','active'),
    ('finished','finished'),
)
class Appointment(models.Model):
    doc = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    pai = models.ForeignKey(Paitent, on_delete=models.CASCADE)
    status = models.CharField(max_length=10 , choices=STATUS_CHOICES )

    date = models.DateTimeField(auto_now_add=True)
    due = models.DateField()
    def __str__(self):
        return str('Dr.'+self.doc.name + '   with   ' + self.pai.name + '  with   '  + self.status)

