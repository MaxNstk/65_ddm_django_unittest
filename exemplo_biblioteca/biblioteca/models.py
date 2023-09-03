from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    pass


class Cliente(models.Model):
    cpf = models.CharField(unique=True, max_length=11, verbose_name="CPF sem . e -")
    nome_completo = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    limite_emrestimos_simultaneos = models.IntegerField(default=2)

    emprestimos = models.ManyToManyField("Livro", through="Empresimo")
   

class Livro(models.Model):
    nome = models.CharField(max_length=255,verbose_name="Nome do livro")
    autor = models.CharField(max_length=255,verbose_name="Nome do autor")
    sinopse = models.TextField(null=True, blank=True)
    data_lancamento = models.DateField(verbose_name="Nome do autor")

    emprestimos = models.ManyToManyField("Cliente", through="Empresimo")

class Emprestimo(models.Model):
    livro = models.ForeignKey("Livro", on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey("Cliente", on_delete=models.DO_NOTHING)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)

    def emprestimo_ativo(self):
        return self.data_devolucao is not None
    
