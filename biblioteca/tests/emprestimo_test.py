from django.test import TestCase

from biblioteca.models.cliente import Cliente
from biblioteca.models.livro import Livro


class EmprestimoTestCase(TestCase):

    def setUp(self) -> None:
        super().setUp()

        cliente_max = Cliente.objects.create(
            cpf='09479306980',
            nome_completo='Max Starke',
            data_nascimento='2022-05-29',
            limite_emprestimos_simultaneos=10
        )
        
        livro_harry_potter_1 = Livro.objects.create(
            nome='Harry Potter e a Pedra Filosofal',
            autor='J K Rolling',
            sinopse='HArry e suas aventuras',
            data_lancamento='2009-10-10',
        )

        livro_harry_potter_2 = Livro.objects.create(
            nome='Harry Potter e a as Reliquias da Morte',
            autor='J K Rolling',
            sinopse='HArry e suas aventuras',
            data_lancamento='2009-10-11',
        )
    

