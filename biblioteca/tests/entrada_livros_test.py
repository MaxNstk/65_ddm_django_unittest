from biblioteca.models.user import User
from biblioteca.models.emprestimo import Emprestimo
from biblioteca.models.entrada_livros import EntradaLivros
from biblioteca.models.livro import Livro
from biblioteca.tests.generic_test import GenericTestCase

from rest_framework.test import APIRequestFactory
from rest_framework import status 
from rest_framework.authtoken.models import Token

class MovimentacaoEstoqueTestCase(GenericTestCase):

    def test_livro_movimentou_estoque(self):

        self.assertEqual(Livro.objects.count(), 2)
        self.assertTrue(User.objects.count() == 1)
        
        EntradaLivros.objects.create(livro=self.livro_harry_potter_1, quantidade=10)
        self.assertEqual(self.livro_harry_potter_1.estoque.quantidade, 10)

        EntradaLivros.objects.create(livro=self.livro_harry_potter_1, quantidade=5)
        self.assertEqual(self.livro_harry_potter_1.estoque.quantidade, 15)

        self.livro_harry_potter_1.emprestar(
            cliente=self.cliente_max,
            quantidade=3
        )

        Emprestimo.objects.emprestar(
            livro=self.livro_harry_potter_1,
            cliente=self.cliente_max,
            quantidade=3    
        )

        self.assertEqual(self.livro_harry_potter_1.estoque.quantidade, 9)

