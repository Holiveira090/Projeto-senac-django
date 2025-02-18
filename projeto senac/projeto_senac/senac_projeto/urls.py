from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'), 
    path('cadastro/', views.cadastro, name='cadastro'),  
    path('historico/', views.historico, name='historico'),
    path('deposito/', views.deposito, name='deposito'),
    path('saque/', views.saque, name='saque'),
]
