from django.db import models
from user import User


class Hike(models.Model):
    hikeID = models.AutoField
    title = models.CharField(max_length=30)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField
    scheduled = models.DateTimeField
    picture = models.ImageField

    def __str__(self):
        return self.title
