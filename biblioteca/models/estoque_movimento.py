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
    entrada_livros = models.ForeignKey('EntradaLivros', on_delete=models.DO_NOTHING, null=True, blank=True)
    tipo = models.IntegerField(choices=tipos)

    def save(self, *args, **kwargs) -> None:
        self.set_tipo()
        super().save(*args, **kwargs)
        self.gerenciar_estoque()
    
    def set_tipo(self):
        if self.emprestimo:
            self.tipo = EstoqueMovimento.SAIDA
        elif self.entrada_livros:
            self.tipo = EstoqueMovimento.ENTRADA
        else:
            raise Exception("Movimentação de estoque sem emprestimo ou entrada de livros informada")

    def gerenciar_estoque(self) -> None:
        if self.tipo == EstoqueMovimento.ENTRADA:
            self.livro.estoque.quantidade += self.quantidade    
        else:
            self.livro.estoque.quantidade -= self.quantidade
        self.livro.estoque.save()