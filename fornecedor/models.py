from django.db import models
class fornecedor (models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    oqfornece = models.CharField(max_length=100)
    comofornece = models.CharField(max_length=100)
def __str__(self):
    return self.nome