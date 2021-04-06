import datetime

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import get_object_or_404

from conta import models
from conta import serializers


# Create your views here.
from conta.exceptions import ContaException


class ContaViewSet(viewsets.ModelViewSet):
    queryset = models.Conta.objects.all().order_by('id_conta')
    serializer_class = serializers.ContaSerializer
    permission_classes = [permissions.AllowAny]


class TransacaoViewSet(viewsets.ModelViewSet):
    queryset = models.Transacao.objects.all().order_by('id_transacao')
    serializer_class = serializers.TransacaoSerializer
    permission_classes = [permissions.AllowAny]


class DepositoAPIView(generics.CreateAPIView):
    serializer_class = serializers.DepositoSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(conta_id=self.kwargs.get('id_conta'))


class SaqueAPIView(generics.CreateAPIView):
    serializer_class = serializers.SaqueSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(conta_id=self.kwargs.get('id_conta'))


class ConsultaSaldoAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.ConsultaSaldoSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        queryset = models.Conta.objects.filter(id_conta__exact=self.kwargs.get('id_conta'))
        return get_object_or_404(queryset)


class BloqueioContaAPIView(generics.UpdateAPIView):
    serializer_class = serializers.BloqueioContaSerializer
    permission_classes = [permissions.AllowAny]


class ExtratoContaAPIView(generics.ListAPIView):
    serializer_class = serializers.ListaTransacoesSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):

        data_inicio = self.request.query_params.get('dataInicio', datetime.date.min)
        data_fim = self.request.query_params.get('dataFim', datetime.date.max)

        return models.Transacao.objects.filter(conta_id__exact=self.kwargs.get('id_conta'), data_transacao__date__range=[data_inicio, data_fim])






