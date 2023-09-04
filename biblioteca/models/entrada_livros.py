from django.db import models

class EntradaLivros(models.Model):

    livro = models.ForeignKey("Livro", on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    # def sa