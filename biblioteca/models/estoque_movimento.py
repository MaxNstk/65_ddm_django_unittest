from django.db import models


class EstoqueMovimento(models.Model):
    ENTRADA = 1
    SAIDA = 2
    livro = models.ForeignKey('Livro', on_delete=models.DO_NOTHING)
