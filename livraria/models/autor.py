from django.db import models


class Autor(models.Model):
    def __str__(self):
        return self.nome

    nome = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
