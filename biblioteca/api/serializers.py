from rest_framework.serializers import ModelSerializer
from biblioteca.models import Estoque, Livro, User, EstoqueMovimento, EntradaLivros, Emprestimo


class EstoqueSerializer(ModelSerializer):

    class Meta:
        model = Estoque
        depth = 2
        fields = '__all__'

class LivroSerializer(ModelSerializer):

    class Meta:
        model = Livro
        depth = 2
        fields = '__all__'
        
class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        depth = 2
        fields = '__all__'


class EstoqueMovimentoSerializer(ModelSerializer):

    class Meta:
        model = EstoqueMovimento
        depth = 2
        fields = '__all__'


class EntradaLivrosSerializer(ModelSerializer):

    class Meta:
        model = EntradaLivros
        depth = 2
        fields = '__all__'


class EmprestimoSerializer(ModelSerializer):

    class Meta:
        model = Emprestimo
        depth = 2
        fields = '__all__'
