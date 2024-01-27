from django.contrib.auth.models import User
from django.db import models
from vendors.models import halls,VendorProfile

class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class bookings(models.Model):
    vendor =models.ForeignKey(VendorProfile, on_delete=models.CASCADE)
    hall =models.ForeignKey(halls,on_delete=models.CASCADE)
    date =models.CharField(max_length=50)
    start_time =models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)
    user =models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return self.vendor

    

