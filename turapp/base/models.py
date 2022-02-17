from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    userName = models.CharField(max_length=20)
    userID = models.AutoField
    userMail = models.EmailField
    name = models.CharField
    userPic = models.ImageField
