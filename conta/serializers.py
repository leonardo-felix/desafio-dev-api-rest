from decimal import Decimal

from rest_framework import serializers
from conta import models


class ContaSerializer(serializers.ModelSerializer):
    idConta = serializers.IntegerField(source='id_conta', read_only=True)
    idPessoa = serializers.PrimaryKeyRelatedField(source='pessoa', queryset=models.Pessoa.objects.all())
    limiteSaqueDiario = serializers.DecimalField(source='limite_saque_diario', max_digits=12, decimal_places=2)
    flagAtivo = serializers.BooleanField(source='flag_ativo')
    tipoConta = serializers.IntegerField(source='tipo_conta')
    dataCriacao = serializers.DateTimeField(source='data_criacao')

    class Meta:
        model = models.Conta
        fields = ('idConta', 'idPessoa', 'saldo', 'limiteSaqueDiario', 'flagAtivo', 'tipoConta', 'dataCriacao')


class TransacaoSerializer(serializers.ModelSerializer):
    idConta = serializers.PrimaryKeyRelatedField(source='conta', queryset=models.Conta.objects.all())
    idTransacao = serializers.IntegerField(source='id_transacao', read_only=True)
    dataTransacao = serializers.DateTimeField(source='data_transacao', label='Data/Hora Transação')

    class Meta:
        model = models.Transacao
        fields = ('idConta', 'idTransacao', 'dataTransacao', 'valor')


class TransacaoInputSerializer(serializers.ModelSerializer):
    idTransacao = serializers.IntegerField(source='id_transacao', read_only=True)
    idConta = serializers.PrimaryKeyRelatedField(source='conta', read_only=True)
    valor = serializers.DecimalField(max_digits=12, decimal_places=2, min_value=Decimal("0.01"))
    dataTransacao = serializers.DateTimeField(source='data_transacao', label='Data/Hora Transação')

    class Meta:
        model = models.Transacao
        fields = ('idTransacao', 'idConta', 'dataTransacao', 'valor')


class DepositoSerializer(TransacaoInputSerializer):
    pass


class SaqueSerializer(TransacaoInputSerializer):

    """
    Validação para salvar o valor como negativo
    """
    def validate_valor(self, value):
        assert value >= 0, "Campo deve vir sempre um valor positivo, depois será alterado para negativo"
        return -value


class ConsultaSaldoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Conta
        fields = ('saldo',)
        fields_read_only = ('saldo',)


class BloqueioContaSerializer(serializers.ModelSerializer):
    flagAtivo = serializers.BooleanField(source='flag_ativo')

    class Meta:
        model = models.Conta
        fields = ('flagAtivo', )


class ListaTransacoesSerializer(serializers.ModelSerializer):
    idTransacao = serializers.IntegerField(source='id_transacao')
    idConta = serializers.PrimaryKeyRelatedField(source='conta', read_only=True)
    valor = serializers.DecimalField(max_digits=12, decimal_places=2, min_value=Decimal("0.01"))
    dataTransacao = serializers.DateTimeField(source='data_transacao')

    #campos filtro
    dataInicio = serializers.DateField(write_only=True)
    dataFim = serializers.DateField(write_only=True)

    class Meta:
        model = models.Transacao
        fields = ('idTransacao', 'idConta', 'dataTransacao', 'valor', 'dataInicio', 'dataFim')
