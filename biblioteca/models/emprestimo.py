from django.db import models
from django.utils import timezone

from biblioteca.managers.emprestimo_manager import EmprestimoManager


class Emprestimo(models.Model):
    
    livro = models.ForeignKey("Livro", on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey("Cliente", on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField(default=1)
    data_emprestimo = models.DateField(default=timezone.now)
    data_estimada_devolucao = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)

    objects = EmprestimoManager()

    def movimentar_estoque(self):
        from biblioteca.models.estoque_movimento import EstoqueMovimento
        EstoqueMovimento.objects.create()

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        self.movimentar_estoque()
    
    