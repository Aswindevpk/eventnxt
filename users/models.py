from django.contrib.auth.models import User
from django.db import models
from vendors.models import VendorProfile
from base.model import BaseModel
import uuid

class UserProfile(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class bookings(BaseModel):
    vendor =models.ForeignKey(VendorProfile, on_delete=models.CASCADE)
    date =models.CharField(max_length=50)
    persons = models.CharField(max_length=10)
    status =models.CharField(max_length=50,null=True,blank=True)
    Total =models.CharField(max_length=50,null=True,blank=True)
    Advance =models.CharField(max_length=50,null=True,blank=True)
    user =models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return self.date

    

