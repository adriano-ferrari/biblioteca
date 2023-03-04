from django import forms
from livro.models import Livros


class CadastroLivro(forms.ModelForm):
    class Meta:
        model = Livros
        fields = '__all__'
