from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default="")

    def __str__(self) -> str:
        return self.name


class Platos(models.Model):
    nombre = models.CharField(max_length=200)
    description = models.TextField(default="")
    producto = models.ManyToManyField(Product, verbose_name='producto', blank=True, symmetrical=False)
    precio = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return self.nombre + ' - ' + str(self.precio)
