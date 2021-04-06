from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from conta import views

router = routers.DefaultRouter()
# router.register(r'contas', views.ContaViewSet)
# router.register(r'contas/(?P<pk>[0-9]+)/deposito', views.DepositoViewSet, basename='deposito'),
# router.register(r'contas/(?P<pk>[0-9]+)/saque', views.SaqueViewSet, basename='saque'),
# router.register(r'transacoes', views.TransacaoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/contas/criar/', views.CriarContaAPIView.as_view()),
    path('api/contas/<int:id_conta>/saldo/', views.ConsultaSaldoAPIView.as_view()),
    path('api/contas/<int:id_conta>/saque/', views.SaqueAPIView.as_view()),
    path('api/contas/<int:id_conta>/deposito/', views.DepositoAPIView.as_view()),
    path('api/contas/<int:id_conta>/bloqueio/', views.BloqueioContaAPIView.as_view()),
    path('api/contas/<int:id_conta>/extrato/', views.ExtratoContaAPIView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
