# Generated by Django 4.2.4 on 2023-09-05 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0003_estoquemovimento_entrada_livros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque',
            name='quantidade',
            field=models.IntegerField(default=0),
        ),
    ]
