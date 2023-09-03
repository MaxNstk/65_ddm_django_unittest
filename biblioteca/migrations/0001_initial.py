# Generated by Django 4.2.4 on 2023-09-03 14:08

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF sem . e -')),
                ('nome_completo', models.CharField(max_length=255)),
                ('data_nascimento', models.DateField()),
                ('limite_emprestimos_simultaneos', models.IntegerField(default=2)),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=1)),
                ('data_emprestimo', models.DateField(default=django.utils.timezone.now)),
                ('data_estimada_devolucao', models.DateField()),
                ('data_devolucao', models.DateField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='biblioteca.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome do livro')),
                ('autor', models.CharField(max_length=255, verbose_name='Nome do autor')),
                ('sinopse', models.TextField(blank=True, null=True)),
                ('data_lancamento', models.DateField(verbose_name='Nome do autor')),
                ('emprestimos', models.ManyToManyField(through='biblioteca.Emprestimo', to='biblioteca.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='EstoqueMovimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='biblioteca.livro')),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('livro', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='biblioteca.livro')),
            ],
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='livro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='biblioteca.livro'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='emprestimos',
            field=models.ManyToManyField(through='biblioteca.Emprestimo', to='biblioteca.livro'),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
