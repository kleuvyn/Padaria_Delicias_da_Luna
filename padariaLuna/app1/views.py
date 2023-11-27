from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomLoginForm


# Views principais
def index(request):
    return render(request, 'app1/index.html')

def cardapio(request):
    return render(request, 'app1/cardapio.html')

def contato(request):
    return render(request, 'app1/contato.html')

def pedidos(request):
    # Adicionei um contexto com os usuários para a página de pedidos
    return render(request, 'app1/pedidos.html', {'users': User.objects.all()})

def qualidade(request):
    return render(request, 'app1/qualidade.html')

def quem_somos(request):
    return render(request, 'app1/quemSomos.html')

def visite_nos(request):
    return render(request, 'app1/visite-nos.html')

# ...
def login_page(request):
    return render(request, 'app1/login.html')
# ...


def user_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('index') 
    else:
        form = CustomLoginForm()

    return render(request, 'app1/index.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')

# View para processar pedidos
def processar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.usuario = request.user
            pedido.save()

            # Adicione uma resposta JSON
            response_data = {
                'message': 'Pedido processado com sucesso!',
                'total': pedido.total(),  # Substitua por lógica real de cálculo de total
            }
            return JsonResponse(response_data)
    else:
        form = PedidoForm()

    return render(request, 'app1/processar_pedido.html', {'form': form})

def user_list(request):
    # Obtém todos os usuários do banco de dados
    users = User.objects.all()

    # Renderiza a lista de usuários em um template
    return render(request, 'app1/user_list.html', {'users': users})