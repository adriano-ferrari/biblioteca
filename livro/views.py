from django.shortcuts import redirect, render
from django.http import HttpResponse

from usuarios.models import Usuario
from .models import Livros, Categoria, Emprestimo
from .forms import CadastroLivro


def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        livros = Livros.objects.filter(usuario=usuario)
        form = CadastroLivro()

        return render(request, 'home.html', {'livros':livros,
                                             'usuario_logado': request.session.get('usuario'),
                                             'form': form})
    else:
        return redirect('/auth/login/?status=2')
    

def visualiza(request, id):
    if request.session.get('usuario'):
        livro = Livros.objects.get(id=id)
        form = CadastroLivro()
        if request.session.get('usuario') == livro.usuario.id:
            categoria_livro = Categoria.objects.filter(usuario = request.session.get('usuario'))
            emprestimos = Emprestimo.objects.filter(livro=livro)

            return render(request, 'visualiza.html', {'livro': livro,
                                                      'categoria_livro': categoria_livro,
                                                      'emprestimos': emprestimos,
                                                      'usuario_logado': request.session.get('usuario'),
                                                      'form': form})
        else:
            return HttpResponse('Esse livro não é seu.')
    return redirect('/auth/login/?status=2')


def cadastra_livro(request):
    if request.method == 'POST':
        form = CadastroLivro(request.POST)

        if form.is_valid():
            form.save()
        else:
            return HttpResponse('DADOS INVÁLIDOS!')