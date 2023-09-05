from django.db import models

class EntradaLivros(models.Model):

    livro = models.ForeignKey("Livro", on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.criar_movimentacao_estoque()

    def criar_movimentacao_estoque(self):
        from biblioteca.models.estoque_movimento import EstoqueMovimento
        EstoqueMovimento.objects.create(
            livro=self.livro,
            quantidade=self.quantidade,
            entrada_livros=self
            )
                                            