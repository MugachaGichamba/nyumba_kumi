from django.db import models

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class Hood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Business(models.Model):
    email = models.EmailField(blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business = models.ForeignKey(Hood, on_delete=models.CASCADE)


class Contact(models.Model):
    email = models.EmailField(blank=False, null=False)
    phone = models.CharField(max_length=100)
    location = models.CharField(max_length=100)