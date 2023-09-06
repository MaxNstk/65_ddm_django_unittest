from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    cpf = models.CharField(unique=True, max_length=11, verbose_name="CPF sem . e -", validators=[
        MinLengthValidator(11, "O CPF deve conter obrigatóriamente 11 digitos")
    ])
    nome_completo = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    limite_emprestimos_simultaneos = models.IntegerField(default=2)

    emprestimos = models.ManyToManyField("Livro", through="Emprestimo")

    def get_qtd_emprestimos_disponiveis(self):
        qtd_emprestimos = self.emprestimo_set.filter(devolvido=False).aggregate(
            models.Sum('quantidade'))['quantidade__sum'] or 0
        return self.limite_emprestimos_simultaneos - qtd_emprestimos

    def emprestar(self, **kwargs):
        from biblioteca.models import Emprestimo
        return Emprestimo.emprestar(cliente=self, **kwargs)