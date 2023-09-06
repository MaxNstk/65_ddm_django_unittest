from rest_framework.viewsets import ModelViewSet
from biblioteca.api.serializers import EstoqueSerializer, LivroSerializer, UserSerializer, EstoqueMovimentoSerializer, EntradaLivrosSerializer, EmprestimoSerializer
from biblioteca.models import Estoque, Livro, User, EstoqueMovimento, EntradaLivros, Emprestimo

from rest_framework import authentication, permissions
from rest_framework.viewsets import ModelViewSet

class LoginRequiredModelViewSet(ModelViewSet):
    authentication_classes = (authentication.SessionAuthentication,authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
    


class EstoqueViewSet(LoginRequiredModelViewSet):
    queryset = Estoque.objects.order_by('pk')
    serializer_class = EstoqueSerializer


class LivroViewSet(LoginRequiredModelViewSet):
    queryset = Livro.objects.order_by('pk')
    serializer_class = LivroSerializer


class UserViewSet(LoginRequiredModelViewSet):
    queryset = User.objects.order_by('pk')
    serializer_class = UserSerializer


class EstoqueMovimentoViewSet(LoginRequiredModelViewSet):
    queryset = EstoqueMovimento.objects.order_by('pk')
    serializer_class = EstoqueMovimentoSerializer


class EntradaLivrosViewSet(LoginRequiredModelViewSet):
    queryset = EntradaLivros.objects.order_by('pk')
    serializer_class = EntradaLivrosSerializer


class EmprestimoViewSet(LoginRequiredModelViewSet):
    queryset = Emprestimo.objects.order_by('pk')
    serializer_class = EmprestimoSerializer
