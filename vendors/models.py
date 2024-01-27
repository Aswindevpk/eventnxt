from django.contrib.auth.models import User
from django.db import models


class categories(models.Model):
    category = models.CharField(max_length= 20)

    def __str__(self):
        return self.category

class halls(models.Model):
    name = models.CharField(max_length= 50)
    category = models.CharField(max_length=50)
    capacity = models.CharField(max_length=3)
    ac = models.BooleanField(default=False)
    desc = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class VendorProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='venues',default=None)
    business_name = models.CharField(max_length=255,default=None)
    city = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15,default=None)
    halls = models.ManyToManyField(halls,default=None)

    def __str__(self):
        return self.venue_name





