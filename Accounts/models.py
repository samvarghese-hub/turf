from django.db import models
from django.db.models.base import Model
from MasterEntry.models import District

class TurfOwnerRegistration(models.Model):
    turfowner_name=models.CharField(max_length=20)
    turfowner_contact=models.CharField(max_length=20,unique=True)
    turfowner_email=models.EmailField(max_length=20,unique=True)
    turfowner_gender=models.CharField(max_length=20)
    turfowner_district=models.ForeignKey(District,on_delete=models.SET_NULL,null=True,verbose_name="District")
    turfowner_address=models.TextField()
    turfowner_image=models.FileField(upload_to='OwnerImage/')
    turfowner_username=models.CharField(max_length=20,unique=True)
    turfowner_password=models.CharField(max_length=20,unique=True)
    turfowner_doj=models.DateField(auto_now_add=True)


