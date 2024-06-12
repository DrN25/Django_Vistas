from django.db import models

# Create your models here.
class Persona(models.Model):
    nombres = models.CharField(max_length=20)
    apellidos = models.TextField()
    edad = models.IntegerField()