from django.db import models


class Categoria(models.Model):
    def __str__(self):
        return self.descricao

    descricao = models.CharField(max_length=100)
