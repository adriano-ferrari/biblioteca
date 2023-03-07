from django.shortcuts import redirect, render
from django.http import HttpResponse

from usuarios.models import Usuario
from .models import Livros, Categoria, Emprestimo
from .forms import CadastroLivro, CategoriaLivro


def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        livros = Livros.objects.filter(usuario=usuario)
        form = CadastroLivro()
        form.fields['usuario'].initial = request.session['usuario']
        form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)

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
            usuario = Usuario.objects.get(id=request.session['usuario'])
            categoria_livro = Categoria.objects.filter(usuario = request.session.get('usuario'))
            emprestimos = Emprestimo.objects.filter(livro=livro)
            form = CadastroLivro()
            form.fields['usuario'].initial = request.session['usuario']
            form.fields['categoria'].queryset = Categoria.objects.filter(usuario=usuario)
            form_categoria = CategoriaLivro()

            return render(request, 'visualiza.html', {'livro': livro,
                                                      'categoria_livro': categoria_livro,
                                                      'emprestimos': emprestimos,
                                                      'usuario_logado': request.session.get('usuario'),
                                                      'form': form,
                                                      'id_livro': id,
                                                      'form_categoria': form_categoria})
        else:
            return HttpResponse('Esse livro não é seu.')
    return redirect('/auth/login/?status=2')


def cadastra_livro(request):
    if request.method == 'POST':
        form = CadastroLivro(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/livro/home')
        else:
            return HttpResponse('DADOS INVÁLIDOS!')


def excluir(request, id):
    livro = Livros.objects.get(id=id).delete()
    return redirect('livro/home')
