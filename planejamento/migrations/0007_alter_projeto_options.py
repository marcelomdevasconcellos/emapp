# Generated by Django 3.2 on 2022-05-01 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planejamento', '0006_alter_projeto_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projeto',
            options={'permissions': (('can_approve_project', 'Pode aprovar projeto'), ('can_submit_project', 'Pode submeter projeto')), 'verbose_name': 'Projeto', 'verbose_name_plural': 'Projetos'},
        ),
    ]
