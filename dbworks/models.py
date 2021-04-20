from django.db import models


class turflogin(models.Model):
    username=models.CharField(max_length=20)

    def __str__(self):
        return self.username
    


class Student(models.Model):
    name=models.CharField(max_length=20)
    rollno=models.CharField(max_length=10)

    def __str__(self):
        return self.name+"("+self.rollno+")"
    
# Create your models here.


class District(models.Model):
    dist=models.CharField(max_length=10)
    names=models.CharField(max_length=10)
    def __str__(self):
        return self.names+"("+self.dist+")"