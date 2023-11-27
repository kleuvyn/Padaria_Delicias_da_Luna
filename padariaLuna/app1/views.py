from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import CustomUser  
from .forms import CustomLoginForm, PedidoForm


def index(request):
    return render(request, 'app1/index.html')

def cardapio(request):
    return render(request, 'app1/cardapio.html')

def contato(request):
    return render(request, 'app1/contato.html')


def pedidos(request):
    return render(request, 'app1/pedidos.html', {'users': CustomUser.objects.all()})

def qualidade(request):
    return render(request, 'app1/qualidade.html')

def quem_somos(request):
    return render(request, 'app1/quemSomos.html')

def visite_nos(request):
    return render(request, 'app1/visite-nos.html')

def login_page(request):
    return render(request, 'app1/login.html')

def user_cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form.errors)
        print(form.cleaned_data) 
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            print('antes login')
            login(request, user)
            print('depois login')
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'app1/cadastro.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        import pdb; pdb.set_trace()
        print(form.errors)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                # return redirect('index')
                return render(request, 'app1/index.html', {'form': form})
        else:
    
            import pdb; pdb.set_trace()
            print(form.errors)
    else:
        form = CustomLoginForm()

    return render(request, 'app1/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')


def processar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.usuario = request.user
            pedido.save()

            response_data = {
                'message': 'Pedido processado com sucesso!',
                'total': pedido.total(),  
            }
            return JsonResponse(response_data)
    else:
        form = PedidoForm()

    return render(request, 'app1/processar_pedido.html', {'form': form})

def user_list(request):
    users = User.objects.all()
    return render(request, 'app1/user_list.html', {'users': users})
