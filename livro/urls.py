from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('visualiza/<int:id>', views.visualiza, name='visualiza'),
    path('cadastra_livro/', views.cadastra_livro, name='cadastra_livro'),
    path('excluir/<int:id>', views.excluir, name='excluir')
]
