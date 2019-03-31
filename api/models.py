from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
