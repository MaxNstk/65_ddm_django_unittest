from django.core.validators import MinLengthValidator
from django.db import models


class Cliente(models.Model):
    cpf = models.CharField(unique=True, max_length=11, verbose_name="CPF sem . e -", validators=[
        MinLengthValidator(11, "O CPF deve conter obrigatóriamente 11 digitos")
    ])
    nome_completo = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    limite_emprestimos_simultaneos = models.IntegerField(default=2)

    emprestimos = models.ManyToManyField("Livro", through="Emprestimo")

    def get_qtd_emprestimos_disponiveis(self):
        emprestimos = self.emprestimos.all()
        emprestimos = emprestimos.filter(data_devolucao__isnull=False)
        return emprestimos.aggregate(
            models.Sum('quantidade'))['quantidade__sum'] or 0

    def emprestar(self, **kwargs):
        from biblioteca.models import Emprestimo
        return Emprestimo.emprestar(cliente=self, **kwargs)