from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    userID = models.AutoField
    #username = models.CharField(max_length=20)
    userMail = models.EmailField
    name = models.CharField(max_length=30)
    userPic = models.ImageField

    def __str__(self):
        return self.userName


class Hike(models.Model):
    hikeID = models.AutoField
    title = models.CharField(max_length=30)
    host = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="hosting")
    description = models.TextField
    scheduled = models.DateTimeField
    picture = models.ImageField
    meetup = models.CharField
    participants = models.ManyToManyField(User, related_name="hikes")

    def joinHike(self, user):
        self.participants.add(user)

    def dropHike(self, user):
        self.participants.remove(user)

    def __str__(self):
        return self.title
