from . import views
from django.urls import path
from .views import user_login, user_list, processar_pedido, user_logout
from .views import user_cadastro
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='logout'),
    path('', views.index, name='index'),
    path('cadastro/', user_cadastro, name='user_cadastro'),  
    path('cardapio/', views.cardapio, name='cardapio'),
    path('contato/', views.contato, name='contato'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('qualidade/', views.qualidade, name='qualidade'),
    path('quem-somos/', views.quem_somos, name='quem_somos'),
    path('visite-nos/', views.visite_nos, name='visite_nos'),
    path('user-list/', user_list, name='user_list'),
    path('processar-pedido/', processar_pedido, name='processar_pedido'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
