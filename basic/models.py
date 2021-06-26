from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True , blank=True)
    def __str__(self):
        return self.user.username
class Paitent(models.Model):
    phone = models.CharField(max_length=10 )
    name = models.CharField(max_length=1000)
    def __str__(self):
        return self.phone

class Appointment(models.Model):
    doc = models.ForeignKey(Doctor , on_delete=models.CASCADE)
    pai = models.ForeignKey(Paitent, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    created_on = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.doc.name + ' with ' + self.pai.name)







class Meds(models.Model):
    item = models.CharField(max_length=100)
    b_price = models.IntegerField(default=0)
    s_price = models.IntegerField(default=0)
    qty = models.IntegerField(default=1)
    
    def __str__(self):
        return self.item
    def get_margin(self):
        return self.s_price - self.b_price

class MedsSlip(models.Model):
    item = models.ForeignKey(Meds , on_delete=models.CASCADE)
    user = models.ForeignKey(Paitent , on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    def __str__(self):
        return self.item.name
    def get_total(self):
        return self.qty*self.item.price

class MedsBill(models.Model):
    meds = models.ManyToManyField(MedsSlip )
    user = models.ForeignKey(Paitent , on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.phone







class Diagnosis(models.Model):
    name = models.CharField(max_length=1000)
    price = models.IntegerField(default=1)
    def __str__(self):
        return self.name

class DiagnoseSlip(models.Model):
    service = models.ForeignKey(Diagnosis , on_delete=models.CASCADE)
    user = models.ForeignKey(Paitent , on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.service.name

class DiagnoseBill(models.Model):
    services = models.ManyToManyField(DiagnoseSlip)
    user = models.ForeignKey(Paitent , on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.phone
