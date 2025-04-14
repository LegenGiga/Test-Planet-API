from django.db import models

# Create your models here.
class Planet(models.Model):
    name = models.CharField(max_length=63)
    radius = models.PositiveBigIntegerField()
    distance = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name