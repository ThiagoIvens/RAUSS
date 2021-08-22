from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('venda_seu_terreno/', views.page_Venda_Seu_Terreno, name='venda_seu_terreno'),
]