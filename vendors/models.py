from django.contrib.auth.models import User
from django.db import models
from base.model import BaseModel
import uuid




class VendorProfile(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='venues',default=None)
    business_name = models.CharField(max_length=255,default=None)
    city = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15,default=None)
    image = models.ImageField(upload_to='images/')
    location = models.TextField(default=None,null=True)
    category = models.CharField(max_length=50)
    capacity = models.CharField(max_length=3)
    ac = models.BooleanField(default=False)
    desc = models.TextField()

    def __str__(self):
        return self.business_name





