from django.test import TestCase

from biblioteca.models.user import User
from biblioteca.models.entrada_livros import EntradaLivros
from biblioteca.models.livro import Livro
from django.test import Client


class GenericTestCase(TestCase):

    def setUp(self) -> None:
        super().setUp()

        self.cliente_max = User.objects.create_user(
            cpf='09479306980',
            nome_completo='Max Starke',
            data_nascimento='2022-05-29',
            limite_emprestimos_simultaneos=10,
            username='max',
            email='max@gmail.com',
            password='supersenha'
        )
        
        self.livro_harry_potter_1 = Livro.objects.create(
            nome='Harry Potter e a Pedra Filosofal',
            autor='J K Rolling',
            sinopse='HArry e suas aventuras',
            data_lancamento='2009-10-10',
        )

        self.livro_harry_potter_2 = Livro.objects.create(
            nome='Harry Potter e a as Reliquias da Morte',
            autor='J K Rolling',
            sinopse='HArry e suas aventuras',
            data_lancamento='2009-10-11',
        )