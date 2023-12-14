from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=256)
    precio = models.IntegerField()
    existencias = models.IntegerField()

    def __str__(self):
        return self.nombre