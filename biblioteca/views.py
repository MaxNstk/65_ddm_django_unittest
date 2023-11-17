from django.shortcuts import render

from biblioteca.models.livro import Livro


def teste_view(request):

    return render(request, 'teste.html', {'livros':Livro.objects.all()})

