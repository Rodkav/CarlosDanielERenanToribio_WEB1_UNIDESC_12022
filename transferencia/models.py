from django.db import models
class transferencia (models.Model):
    tipo = models.CharField(max_length=100)
    codificacao = models.CharField(max_length=100)
    

def __str__(self):
    return self.nome