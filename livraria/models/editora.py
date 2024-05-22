from django.db import models


class Editora(models.Model):
    def __str__(self):
        return self.nome

    nome = models.CharField(max_length=100)
    site = models.URLField(null=True, blank=True)
