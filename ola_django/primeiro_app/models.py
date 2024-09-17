from django.db import models

# Create your models here.
class NovaModel(models.Model):
    nome = models.CharField(max_length=45)

    def __str__(self) -> str:
        return sel.nome
