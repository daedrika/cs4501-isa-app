from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime


class Sample(models.Model):
    name = models.CharField(max_length=50)
    purchase_count = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    current_seller = models.ForeignKey(Musician, null=True, blank=True, on_delete=models.SET_NULL)
    buyers = models.ManyToManyField(Musician, blank=True)
    minute_length = models.IntegerField(default=0)
    second_length = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Musician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    follower_count = models.IntegerField(default=0)
    balance = models.DecimalField(max_digits=11, decimal_places=2)
    rating = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username
    
