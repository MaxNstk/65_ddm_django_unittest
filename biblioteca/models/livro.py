from django.db import models

from biblioteca.models.estoque import Estoque


class Livro(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome do livro")
    autor = models.CharField(max_length=255, verbose_name="Nome do autor")
    sinopse = models.TextField(null=True, blank=True)
    data_lancamento = models.DateField(verbose_name="Nome do autor")

    emprestimos = models.ManyToManyField("Cliente", through="Emprestimo")

    def get_estoque_disponivel(self):
        from biblioteca.models.estoque import Estoque
        return Estoque.objects.get(livro=self).quantidade

    def emprestar(self, **kwargs):
        from biblioteca.models.emprestimo import Emprestimo
        return Emprestimo.objects.emprestar(livro=self, **kwargs)
    
    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        Estoque.objects.get_or_create(livro=self)
