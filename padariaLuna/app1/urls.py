from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('cardapio/', views.cardapio, name='cardapio'),
    path('contato/', views.contato, name='contato'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('qualidade/', views.qualidade, name='qualidade'),
    path('quem-somos/', views.quem_somos, name='quem_somos'),
    path('visite-nos/', views.visite_nos, name='visite_nos'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
