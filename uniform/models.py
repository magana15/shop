from django.db import models

class Uniform(models.Model):
    name = models.CharField(max_length= 100)
    colour = models.CharField(max_length= 100)
    size = models.CharField(max_length = 3)

    def __str__(self):
        return f"{self.colour} {self.name}"

