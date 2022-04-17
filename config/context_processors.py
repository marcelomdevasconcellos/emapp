import datetime
from . import settings
from planejamento.choices import (
    STATUS_PENDENTE,
    STATUS_NEGADO,
    STATUS_APROVADO,
    STATUS_PROPOSTA,
    STATUS_CADASTRADO
)


def admin_context(request):
    return {
        'MEDIA_URL': settings.MEDIA_URL,
        'STATUS_PENDENTE': STATUS_PENDENTE,
        'STATUS_NEGADO': STATUS_NEGADO,
        'STATUS_APROVADO': STATUS_APROVADO,
        'STATUS_PROPOSTA': STATUS_PROPOSTA,
        'STATUS_CADASTRADO': STATUS_CADASTRADO,
    }
