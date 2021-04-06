"""desafio_dev_api_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from conta import views

router = routers.DefaultRouter()
# router.register(r'contas', views.ContaViewSet)
# router.register(r'contas/(?P<pk>[0-9]+)/deposito', views.DepositoViewSet, basename='deposito'),
# router.register(r'contas/(?P<pk>[0-9]+)/saque', views.SaqueViewSet, basename='saque'),
router.register(r'transacoes', views.TransacaoViewSet)

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
    path('openapi', get_schema_view(
                title="Your Project",
                description="API for all things …",
                version="1.0.0"
            ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
            template_name='swagger-ui.html',
            extra_context={'schema_url': 'openapi-schema'}
        ), name='swagger-ui'),
]
