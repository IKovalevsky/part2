from django.db import models
from pydantic import BaseModel


# Create your models here.

class Work(models.Model):
    articul = models.TextField()
    nameArticul = models.TextField(max_length=100)
    brand = models.TextField(max_length=100)

    def __str__(self):
        return self.articul
