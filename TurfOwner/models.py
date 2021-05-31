from django.db import models
from MasterEntry.models import District
from Accounts.models import TurfOwnerRegistration

class TurfManagerRegistration(models.Model):
    turfManager_name=models.CharField(max_length=20)
    turfManager_contact=models.CharField(max_length=20,unique=True)
    turfManager_email=models.EmailField(max_length=20,unique=True)
    turfManager_gender=models.CharField(max_length=20)
    turfManager_district=models.ForeignKey(District,on_delete=models.SET_NULL,null=True,verbose_name="District")
    turfManager_address=models.TextField()
    turfManager_image=models.FileField(upload_to='ManagerImage/')
    turfManager_username=models.CharField(max_length=20,unique=True)
    turfManager_password=models.CharField(max_length=20,unique=True)
    turfManager_doj=models.DateField(auto_now_add=True)
    turfManager_isactive=models.BooleanField(default=True)
    turfManager_owner=models.ForeignKey(TurfOwnerRegistration,on_delete=models.SET_NULL,null=True,verbose_name="Owner")

