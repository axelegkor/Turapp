from email.policy import default
from django.db import models
#from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


# class User(AbstractUser):
#userID = models.AutoField
#username = models.CharField(max_length=20)
#userMail = models.EmailField
#name = models.CharField(max_length=30)
#picture = models.ImageField


class Hike(models.Model):
    #hikeID = models.AutoField
    title = models.CharField(max_length=30, null=False)
    host = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="hosting")
    description = models.TextField(null=False)
    scheduled = models.DateTimeField(default=None, blank=True, null=True)
    #picture = models.ImageField(default=None)
    meetup = models.CharField(max_length=50, null=False)
    participants = models.ManyToManyField(User, related_name="participants")

    def joinHike(self, user):
        self.participants.add(user)

    def dropHike(self, user):
        self.participants.remove(user)

    def __str__(self):
        return self.title
