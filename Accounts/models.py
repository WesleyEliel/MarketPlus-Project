import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils import timezone
from Products.models import Product


# Create your models here.


class Address(models.Model):
    location = models.CharField(max_length=100)
    location_point = models.CharField(max_length=100)


class UserProfile(User):
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True)
    date_of_birth = models.DateField(help_text='Enter your Birthday following this format YYYY/MM/DD')
    profession = models.CharField(max_length=100,help_text="Help us to provide you analytics Articles")
    postal_code = models.CharField(max_length=40, blank=True)
    phone = models.CharField(max_length=25)
    country = models.CharField(max_length=20, blank=True)
    city_town = models.CharField(max_length=30, blank=True)
    address = models.ForeignKey(Address, null=True, on_delete=models.CASCADE, related_name='a_user_first_address',
                                   blank=True)
    another_address = models.ForeignKey(Address, null=True, on_delete=models.CASCADE, related_name='a_user_other_address',
                                           blank=True)
    other_note = models.CharField(max_length=220, null=True, blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

