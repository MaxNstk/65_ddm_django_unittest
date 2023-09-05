from django.db import models
from django.utils import timezone
from datetime import date, timedelta
import datetime
from django.db import models
from biblioteca.exceptions.limite_emprestimos_exception import LimiteEmprestimosException
from biblioteca.exceptions.livro_sem_estoque_exception import LivroSemEstoqueException

from biblioteca.models.cliente import Cliente
from biblioteca.models.estoque_movimento import EstoqueMovimento
from biblioteca.models.livro import Livro


class EmprestimoManager(models.Manager):

    def emprestar(self, 
        livro:Livro, cliente:Cliente, 
        data_emprestimo:date=datetime.datetime.today(), 
        data_estimada_devolucao:date=(datetime.datetime.today()-datetime.timedelta(days=30)),
        quantidade:int=1,
    ):
        from biblioteca.models.emprestimo import Emprestimo

        # validando cliente
        if cliente.get_qtd_emprestimos_disponiveis() < quantidade:
            raise LimiteEmprestimosException(f"O cliente {cliente.nome_completo} \
                                              não pode mais realizar emprestimos")
        
        # validando livro
        estoque_disponivel = livro.get_estoque_disponivel()
        if estoque_disponivel < quantidade:
            raise LivroSemEstoqueException(f"O livro {livro.nome} não tem estoque suficiente. \
                                Solicitado {quantidade}, disponível {estoque_disponivel}")
        
        return Emprestimo.objects.create(livro=livro, cliente=cliente, quantidade=quantidade,
                   data_emprestimo=data_emprestimo, data_estimada_devolucao=data_estimada_devolucao)
    