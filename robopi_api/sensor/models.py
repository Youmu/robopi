from django.db import models

# Create your models here.
from django.db import models


class Sensor(models.Model):
    roll_data = models.IntegerField(default=0)
    pitch_data = models.IntegerField(default=0)
    yaw_data = models.IntegerField(default=0)