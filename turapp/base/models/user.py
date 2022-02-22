from django.db import models
from django.contrib.auth.models import AbstractUser
from hike import Hike


class User(AbstractUser):
    userID = models.AutoField
    userName = models.CharField(max_length=20)
    userMail = models.EmailField
    name = models.CharField(max_length=30)
    userPic = models.ImageField
    hikes = models.ManyToManyField(Hike, related_name="participants")

    def joinHike(self, hike):
        self.hikes.add(hike)

    def dropHike(self, hike):
        self.hikes.remove(hike)

    def __str__(self):
        return self.userName
