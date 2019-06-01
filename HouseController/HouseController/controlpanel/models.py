from django.db import models


class Temperature(models.Model):

    temperature = models.FloatField()
    date = models.DateTimeField()

    def __str__(self):
        return self.temperature

