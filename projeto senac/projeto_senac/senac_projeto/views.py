from django.shortcuts import render

# Função para renderizar o template login.html
def login(request):
    return render(request, 'senac_projeto/login.html')

def cadastro(request):
    return render(request, 'senac_projeto/cadastro.html')

def historico(request):
    return render(request, 'senac_projeto/historico.html')

def deposito(request):
    return render(request, 'senac_projeto/deposito.html')

def saque(request):
    return render(request, 'senac_projeto/saque.html')