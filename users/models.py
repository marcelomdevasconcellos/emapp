from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    nome = models.CharField(
        "Nome Completo",
        blank=True,
        max_length=255)
    telefone = models.CharField(
        'Telefone(s)',
        max_length=255, )
    cpf = models.CharField(
        'CPF (sem pontuação)',
        max_length=11,
        unique=True,
        blank=True,
        null=True, )

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.nome:
            return self.nome
        else:
            return self.username

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'