from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app1/index.html')

def cardapio(request):
    return render(request, 'app1/cardapio.html')

def contato(request):
    return render(request, 'app1/contato.html')

def pedidos(request):
    return render(request, 'app1/pedidos.html')

def qualidade(request):
    return render(request, 'app1/qualidade.html')

def quem_somos(request):
    return render(request, 'app1/quemSomos.html')

def visite_nos(request):
    return render(request, 'app1/visite-nos.html')