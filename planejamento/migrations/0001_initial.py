# Generated by Django 3.2 on 2022-04-17 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acompanhamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Modificado em')),
                ('data', models.DateTimeField(verbose_name='Data/Hora')),
                ('descricao', models.TextField(verbose_name='Descricao')),
            ],
            options={
                'verbose_name': 'Acompanhamento',
                'verbose_name_plural': 'Acompanhamentos',
            },
        ),
        migrations.CreateModel(
            name='Financeiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Modificado em')),
                ('ano', models.IntegerField(choices=[(2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021'), (2022, '2022')], verbose_name='Ano')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Planejamento Financeiro',
                'verbose_name_plural': 'Planejamento Financeiro',
            },
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Modificado em')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('detalhamento', models.TextField(verbose_name='Detalhamento')),
                ('endereco', models.CharField(max_length=200, verbose_name='Endereço')),
                ('latitude', models.DecimalField(blank=True, decimal_places=12, max_digits=15, null=True, verbose_name='Latitude')),
                ('longitude', models.DecimalField(blank=True, decimal_places=12, max_digits=15, null=True, verbose_name='Longitude')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
                ('data_aprovacao', models.DateTimeField(blank=True, null=True, verbose_name='Data de aprovação')),
                ('prazo_execucao', models.IntegerField(verbose_name='Prazo de execução (meses)')),
                ('status', models.IntegerField(choices=[(0, 'Cadastrado'), (1, 'Proposta'), (2, 'Aprovado'), (3, 'Pendente'), (4, 'Negado')], default=0, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Projeto',
                'verbose_name_plural': 'Projetos',
            },
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Modificado em')),
                ('nome', models.CharField(max_length=60, verbose_name='Nome')),
                ('telefone', models.CharField(max_length=150, verbose_name='Telefone(s)')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Responsável',
                'verbose_name_plural': 'Responsáveis',
            },
        ),
    ]
