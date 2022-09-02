from enum import Flag
from django.db import models

# Create your models here.

# service model #

class Services(models.Model):
    serviceName = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='services', null=False)
    about = models.TextField(null=False)
    date = models.DateField(auto_now=False, auto_now_add=False, null=False)

    def __str__(self) -> str:
        return self.serviceName

# service model #

# our counsellors  #
class Counsellors(models.Model):
    name = models.CharField(max_length=100)
    profilePic = models.ImageField(upload_to='counsellor',null= False)
    qualifications = models.CharField(max_length=200)
    about = models.TextField(blank=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=12)
    CITY_CHOICES = (
        ('Chandigarh','Chandigarh'),
        ('Sangur','Sangur'),
        ('Amritsar','Amritsar'),
        ('Ludhiana','Ludhiana'),
        ('Moga','Moga'),
        ('Sunam','Sunam'),
        ('other','other'),
    )
    city = models.CharField(max_length=100, choices=CITY_CHOICES, default='Select City')
    EXPERTISE_CHOICES = (
        ('Career', 'Career'),
        ('Relationship', 'Relationship'),
        ('Legal Services', 'Legal Services'),
    )
    expertise = models.CharField(max_length=100, choices=EXPERTISE_CHOICES)
    appointment = models.URLField(max_length=200)
    insta = models.URLField(max_length=200)
    facebook = models.URLField(max_length=200)
# our counsellors  #

# FAQ #
class FAQ(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    

    def __str__(self) -> str:
        return self.question
# FAQ #
