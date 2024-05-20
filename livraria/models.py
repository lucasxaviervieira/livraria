from django.db import models

# Create your models here.


class Categoria(models.Model):
    def __str__(self):
        return self.descricao

    descricao = models.CharField(max_length=100)


class Editora(models.Model):
    def __str__(self):
        return self.nome

    nome = models.CharField(max_length=100)
    site = models.URLField(null=True, blank=True)
