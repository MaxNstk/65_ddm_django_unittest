from django.db import models


class Estoque(models.Model):
    livro = models.OneToOneField("Livro", on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField(default=0)
