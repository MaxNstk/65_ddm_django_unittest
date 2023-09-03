from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class Usuario(AbstractUser):
    pass


class Cliente(models.Model):
    cpf = models.CharField(unique=True, max_length=11, verbose_name="CPF sem . e -")
    nome_completo = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    limite_emprestimos_simultaneos = models.IntegerField(default=2)

    emprestimos = models.ManyToManyField("Livro", through="Emprestimo")


class Livro(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome do livro")
    autor = models.CharField(max_length=255, verbose_name="Nome do autor")
    sinopse = models.TextField(null=True, blank=True)
    data_lancamento = models.DateField(verbose_name="Nome do autor")

    emprestimos = models.ManyToManyField("Cliente", through="Emprestimo")


class Estoque(models.Model):
    livro = models.OneToOneField("Livro", on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField()


class EstoqueMovimento(models.Model):
    ENTRADA = 1
    SAIDA = 2
    livro = models.ForeignKey('Livro', on_delete=models.DO_NOTHING)


class Emprestimo(models.Model):
    livro = models.ForeignKey("Livro", on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey("Cliente", on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField(default=1)
    data_emprestimo = models.DateField(default=timezone.now)
    data_estimada_devolucao = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)

    def emprestimo_ativo(self):
        return self.data_devolucao is not None
