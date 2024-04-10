from django.db import models

class Pacient(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    position = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name
