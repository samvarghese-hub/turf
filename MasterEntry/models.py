from django.core import validators
from django.db import models
from django.core.validators import RegexValidator
from django.db.models.base import Model



isalphanumericValidation = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')
# Create your models here.


class District(models.Model):
    district_name=models.CharField("District:",max_length=10,unique=True,validators=[isalphanumericValidation])

    def __str__(self):
        return self.district_name

class Place(models.Model):
    place_name=models.CharField("Place:",max_length=20,unique=True,validators=[isalphanumericValidation])
    place_District=models.ForeignKey(District,on_delete=models.SET_NULL,null=True,verbose_name="District")

    def __str__(self):
        return self.place_name

    