# Generated by Django 3.2 on 2022-04-17 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planejamento', '0004_projeto_data_ultimo_acompanhamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='data_ultimo_acompanhamento',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data do último acompanhamento'),
        ),
    ]
