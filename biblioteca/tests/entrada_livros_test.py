from django.test import TestCase

from biblioteca.models.cliente import Cliente
from biblioteca.models.emprestimo import Emprestimo
from biblioteca.models.entrada_livros import EntradaLivros
from biblioteca.models.livro import Livro
from biblioteca.tests.generic_test import GenericTestCase


class MovimentacaoEstoqueTestCase(GenericTestCase):

    def test_livro_movimentou_estoque(self):
        
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
