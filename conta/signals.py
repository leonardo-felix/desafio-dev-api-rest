from decimal import Decimal

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import Sum

from conta import models
from conta.exceptions import ContaException


@receiver(post_save, sender=models.Transacao)
def atualizar_saldo(sender, **kwargs):
    instancia = kwargs.get('instance')
    soma_saldo = models.Transacao.objects.filter(conta__exact=instancia.conta.id_conta).aggregate(Sum('valor'))
    conta = models.Conta.objects.get(pk=instancia.conta.id_conta)

    if soma_saldo:
        conta.saldo = soma_saldo['valor__sum']
        conta.save(update_fields=['saldo'])


@receiver(pre_save, sender=models.Transacao)
def verificacoes_pre_save(sender, **kwargs):
    transacao = kwargs.get('instance')
    conta = models.Conta.objects.get(pk=transacao.conta.id_conta)

    if not conta.flag_ativo:
        raise ContaException('Conta com bloqueio. Não é possível efetuar transações.')

    dia = transacao.data_transacao
    # valor negativo é considerado um saque.. então
    saque_dia = models.Transacao.objects.filter(conta__exact=transacao.conta.id_conta, valor__lte=Decimal("-0.01"),
                                                data_transacao__date=dia).aggregate(Sum('valor'))['valor__sum'] or 0
    valor_saque_total = saque_dia + transacao.valor

    if (conta.saldo+transacao.valor) < 0:
        raise ContaException('Saque maior que saldo disponível.')

    if abs(valor_saque_total) > abs(conta.limite_saque_diario):
        raise ContaException('Valor limite do saque diário ultrapassado.')
