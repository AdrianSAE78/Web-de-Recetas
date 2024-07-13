from django.db import models

# Create your models here.
class Recetas(models.Model):
    name = models.CharField(max_length=100, null=False)
    RECIPES_TYPES={
        ("P", "Postre"),
        ("B", "Bebida"),
        ("F", "Plato Fuerte"),
        ("E", "Entrada")
    }
    type = models.CharField(max_length=30, choices=RECIPES_TYPES, null=False)
    ingredients = models.CharField(max_length=500, null=False)

    def __str__(self) -> str:
        return self.name