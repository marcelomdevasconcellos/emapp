# Generated by Django 3.2 on 2022-04-17 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('planejamento', '0001_initial'),
        ('institucional', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contrib', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='responsavel',
            name='created_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='responsavel_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AddField(
            model_name='responsavel',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='responsavel_update_by', to=settings.AUTH_USER_MODEL, verbose_name='Modificado por'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='created_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='projeto_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='responsavel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='projeto_responsavel', to='planejamento.responsavel', verbose_name='Responsável'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='secretaria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='projeto_secretaria', to='institucional.secretaria'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='projeto_orcamento', to='contrib.projetotipo'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='projeto_orcamento', to='contrib.unidadetipo'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='projeto_update_by', to=settings.AUTH_USER_MODEL, verbose_name='Modificado por'),
        ),
        migrations.AddField(
            model_name='financeiro',
            name='created_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='financeiro_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AddField(
            model_name='financeiro',
            name='projeto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='financeiro_projeto', to='planejamento.projeto'),
        ),
        migrations.AddField(
            model_name='financeiro',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='financeiro_update_by', to=settings.AUTH_USER_MODEL, verbose_name='Modificado por'),
        ),
        migrations.AddField(
            model_name='acompanhamento',
            name='created_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='acompanhamento_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AddField(
            model_name='acompanhamento',
            name='projeto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='acompanhamento_projeto', to='planejamento.projeto'),
        ),
        migrations.AddField(
            model_name='acompanhamento',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='acompanhamento_update_by', to=settings.AUTH_USER_MODEL, verbose_name='Modificado por'),
        ),
        migrations.AlterUniqueTogether(
            name='financeiro',
            unique_together={('projeto', 'ano')},
        ),
    ]