from django.db import models
from django.contrib.auth.models import User

# Player model with 4 fields as required by the question
class Player(models.Model):
    user          = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name          = models.CharField(max_length=200)
    jersey_number = models.CharField(max_length=10)
    position      = models.CharField(max_length=100)
    team          = models.CharField(max_length=200)

    def __str__(self):
        return self.name
