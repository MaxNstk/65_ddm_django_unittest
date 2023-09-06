from rest_framework.viewsets import ModelViewSet
from biblioteca.api.serializers import EstoqueSerializer, LivroSerializer, UserSerializer, EstoqueMovimentoSerializer, EntradaLivrosSerializer, EmprestimoSerializer
from biblioteca.models import Estoque, Livro, User, EstoqueMovimento, EntradaLivros, Emprestimo


class LoginRequiredModelViewset(ModelViewSet):
    permission_classes = 


class EstoqueViewSet(ModelViewSet):
    queryset = Estoque.objects.order_by('pk')
    serializer_class = EstoqueSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.order_by('pk')
    serializer_class = LivroSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.order_by('pk')
    serializer_class = UserSerializer


class EstoqueMovimentoViewSet(ModelViewSet):
    queryset = EstoqueMovimento.objects.order_by('pk')
    serializer_class = EstoqueMovimentoSerializer


class EntradaLivrosViewSet(ModelViewSet):
    queryset = EntradaLivros.objects.order_by('pk')
    serializer_class = EntradaLivrosSerializer


class EmprestimoViewSet(ModelViewSet):
    queryset = Emprestimo.objects.order_by('pk')
    serializer_class = EmprestimoSerializer
