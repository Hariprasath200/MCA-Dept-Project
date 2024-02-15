from django.db import models
import datetime
import os 
from django.db import models


def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)


class Image(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="picture/")

    def __str__(self) :
        return self.name
    
    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Image"


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    description = models.CharField(max_length=255)

class Registration(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=10000)
    email = models.CharField(max_length=100)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
