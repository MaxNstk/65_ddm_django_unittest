from django.test import TestCase

from biblioteca.models.user import User
from biblioteca.models.livro import Livro
from django.test import Client

class UserRegistrationForm:
    pass

class EmprestimoTestCase(TestCase):

    def setUp(self) -> None:
        super().setUp()

        cliente_max = User.objects.create(
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
    
    def test_details(self):

        self.client = Client()

        response = self.client.get("/teste/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "teste.html")  
        self.assertContains(response, "Harry Potter e a Pedra Filosofal")
        self.assertEqual(len(response.context["livros"]), 2)

    def test_redirect_after_login(self):
        self.client = Client()
        login_data = {"username": "max", "password": "supersenha"}
        response = self.client.post("/login/", data=login_data, follow=True) 
        self.assertRedirects(response, "/dashboard/")

def test_user_registration_form(self):
    form_data = {
        "cpf": "12345678901",
        "nome_completo": "João da Silva",
        "data_nascimento": "1990-01-01",
        "username": "joao",
        "email": "joao@example.com",
        "password1": "senhasegura",
        "password2": "senhasegura",
    }
    form = UserRegistrationForm(data=form_data)
    self.assertTrue(form.is_valid())

def test_user_authentication(self):
    self.client = Client()
    login_data = {"username": "max", "password": "supersenha"}
    response = self.client.post("/login/", data=login_data, follow=True)
    self.assertTrue(response.context["user"].is_authenticated)
