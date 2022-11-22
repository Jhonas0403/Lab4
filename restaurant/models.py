from django.db import models

# Create your models here.
class Project(models.Model):
    name= models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name= models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name

class Platos(models.Model):
    nombre = models.CharField(max_length=200)
    description = models.TextField()
    producto = models.ForeignKey(Product, on_delete = models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nombre+'-'+self.producto.name
