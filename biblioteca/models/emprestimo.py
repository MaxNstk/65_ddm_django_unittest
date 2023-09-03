from django.db import models
from django.utils import timezone


class Emprestimo(models.Model):
    livro = models.ForeignKey("Livro", on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey("Cliente", on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField(default=1)
    data_emprestimo = models.DateField(default=timezone.now)
    data_estimada_devolucao = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)