from django.shortcuts import redirect, render
from django.http import HttpResponse

from usuarios.models import Usuario
from .models import Livros, Categoria



def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        livros = Livros.objects.filter(usuario=usuario)
        return render(request, 'home.html', {'livros':livros})
    else:
        return redirect('/auth/login/?status=2')
    

def visualiza(request, id):
    if request.session.get('usuario'):
        livro = Livros.objects.get(id=id)
        if request.session.get('usuario') == livro.usuario.id:
            categoria_livro = Categoria.objects.filter(usuario = request.session.get('usuario'))

            return render(request, 'visualiza.html', {'livro': livro, 'categoria_livro': categoria_livro})
        else:
            return HttpResponse('Esse livro não é seu.')
    return redirect('/auth/login/?status=2')
