from django.db import models


class SimpleThing(models.Model):
    name = models.CharField(max_length=255)
    family = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} {self.family}'
