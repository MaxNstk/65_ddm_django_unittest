from django.db import models
from django.utils import timezone

from biblioteca.managers.emprestimo_manager import EmprestimoManager


class Emprestimo(models.Model):
    
    livro = models.ForeignKey("Livro", on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey("User", on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField(default=1)
    data_emprestimo = models.DateField(default=timezone.now)
    data_estimada_devolucao = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)
    devolvido = models.BooleanField(default=False)

    objects = EmprestimoManager()

    def movimentar_estoque(self):
        from biblioteca.models.estoque_movimento import EstoqueMovimento
        EstoqueMovimento.objects.create(
            livro=self.livro,
            quantidade=self.quantidade,
            emprestimo=self
        )
    
    def verificar_devolucao(self):
        if self.data_devolucao: self.devolvido = True

    def save(self, *args, **kwargs) -> None:
        self.verificar_devolucao()
        super().save(*args, **kwargs)
        self.movimentar_estoque()
    
    