from django.db import models
from django.contrib.auth.models import User


class EnArriendo(models.Model):
    titulo = models.CharField(max_length=128)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Detalle(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=128)
    desc = models.TextField()
    ancho = models.CharField(max_length=100)
    largo = models.CharField(max_length=100)
    esta = models.ForeignKey(EnArriendo, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.desc[10]}...'
