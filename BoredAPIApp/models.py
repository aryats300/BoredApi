# boredapi_app/models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    registration_type = models.CharField(max_length=100)
    # Add any other fields you need for user registration

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Add any other fields you need for activities
