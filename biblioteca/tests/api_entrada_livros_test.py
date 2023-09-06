from django.test import Client
from django.urls import reverse

from biblioteca.models.user import User
from biblioteca.models.emprestimo import Emprestimo
from biblioteca.models.entrada_livros import EntradaLivros
from biblioteca.models.livro import Livro
from biblioteca.tests.generic_test import GenericTestCase

from rest_framework.test import APIRequestFactory
from rest_framework import status 
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

class ApiEntradaLivrosTestCase(APITestCase):

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

    def test_api_livro_movimentou_estoque(self):

        response = self.client.get(reverse('user-list'), format='json')
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

        token = Token.objects.create(user=self.cliente_max)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
        response = self.client.get(reverse('user-list'), format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        
        response = self.client.post(reverse('livro-list'), {'algo_sem_sentido':'AAAAAAAAA'}, format='json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post(reverse('livro-list'),
                                {'nome':'meu livro',
                                'autor':'eu mesmo',
                                'sinopse':'é isso',
                                'data_lancamento':'2023-06-06'}
        , format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
    
