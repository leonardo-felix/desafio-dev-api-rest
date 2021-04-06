from decimal import Decimal

from django.db import models


# Create your models here.

class Pessoa(models.Model):
    id_pessoa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=250)
    cpf = models.CharField(max_length=12, unique=True)
    data_nascimento = models.DateField()

    class Meta:
        ordering = ('id_pessoa',)

    def __str__(self):
        return f'{self.nome} - {self.cpf} ({self.id_pessoa})'


class Conta(models.Model):
    id_conta = models.AutoField(primary_key=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal("0"))
    limite_saque_diario = models.DecimalField(max_digits=12, decimal_places=2)
    flag_ativo = models.BooleanField(default=True)
    tipo_conta = models.IntegerField(default=1)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id_conta',)

    def __unicode__(self):
        return f"{self.id_conta} - {self.pessoa.nome}"

    def __str__(self):
        return self.__unicode__()


class Transacao(models.Model):
    id_transacao = models.AutoField(primary_key=True)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    data_transacao = models.DateTimeField()

    class Meta:
        ordering = ('id_transacao',)
