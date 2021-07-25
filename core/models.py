from typing import Sized
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator



class Team(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=600)
    image = models.ImageField(default = '')
    occupation = models.CharField(default='Marketing manager', max_length=100)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=600)
    image = models.ImageField(default = '')
    occupation = models.CharField(default='Marketing manager', max_length=100)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    image = models.ImageField(default = 'shop.png')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    message = models.TextField(max_length=700)

    def __str__(self):
        return self.full_name