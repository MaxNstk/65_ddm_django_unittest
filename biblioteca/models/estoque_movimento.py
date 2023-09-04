from typing import Iterable, Optional
from django.db import models


class EstoqueMovimento(models.Model):
    ENTRADA = 1
    SAIDA = 2

    tipos = (
        (ENTRADA, 'Entrada'),
        (SAIDA, 'Saída'),
    )

    livro = models.ForeignKey('Livro', on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField(default=1)
    emprestimo = models.ForeignKey('Emprestimo', on_delete=models.DO_NOTHING, null=True, blank=True)
    tipo = models.IntegerField(choices=tipos)

    # classmethod
    # def 

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
                
        if self.tipo == EstoqueMovimento.ENTRADA:
            self.livro.estoque.quantidade += self.quantidade    
        else:
            self.livro.estoque.quantidade -= self.quantidade
        self.livro.estoque.save()