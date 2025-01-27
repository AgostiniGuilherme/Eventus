from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def principal(request):
    template = loader.get_template('principal.html')
    return HttpResponse(template.render())

def eventos(request):
    template = loader.get_template('eventos.html')
    context = {
        'eventos': [
            {
                "nome": "Festa de Aniversário",
                "local": "Casa do João",
                "data": "2024-12-20",
                "descricao": "Comemoração do aniversário do João com muita diversão!"
            },
            {
                "nome": "Workshop de Python",
                "local": "Centro de Tecnologia",
                "data": "2024-12-15",
                "descricao": "Workshop para iniciantes em Python, com foco em desenvolvimento web."
            },
            {
                "nome": "Concerto de Natal",
                "local": "Teatro Municipal",
                "data": "2024-12-24",
                "descricao": "Concerto de música clássica para celebrar o Natal."
            },
            {
                "nome": "Cineclube - Exibição de Filme",
                "local": "Cinemateca",
                "data": "2024-12-18",
                "descricao": "Exibição de filmes independentes seguidos de debate sobre a produção."
            }
        ]
    }
    return HttpResponse(template.render(context, request))

@login_required
def meus_eventos(request):  # Lista os eventos onde o usuário participa ou é organizador
    user = request.user  # Obtendo o usuário logado

    template = loader.get_template('meus_eventos.html')  # Carrega o template meus_eventos.html
    context = {
        'eventos': [

          ]
    }

    return HttpResponse(template.render(context, request)) 

def evento_detalhes(request, id):
    eventos = [
        {
            "id": 1,
            "nome": "Festa de Aniversário",
            "local": "Casa do João",
            "data": "2024-12-20",
            "descricao": "Comemoração do aniversário do João com muita diversão!"
        },
        {
            "id": 2,
            "nome": "Workshop de Python",
            "local": "Centro de Tecnologia",
            "data": "2024-12-15",
            "descricao": "Workshop para iniciantes em Python, com foco em desenvolvimento web."
        },
        {
            "id": 3,
            "nome": "Concerto de Natal",
            "local": "Teatro Municipal",
            "data": "2024-12-24",
            "descricao": "Concerto de música clássica para celebrar o Natal."
        },
    ]
    
    evento = eventos[id-1] 
    template = loader.get_template('eventos_detalhes.html')
    context = {
        'evento': evento,
    }
    return HttpResponse(template.render(context, request))

def cadastrar(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso! Faça login.')
            return redirect('principal')
    else:
        form = CustomUserCreationForm()
    return render(request, 'cadastrar.html', {'form': form})

def logar(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Autentica o usuário usando o nome de usuário obtido (que pode ser um email)
            user = authenticate(request, username=username_or_email, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, "Login bem-sucedido!")
                return redirect('principal')  # Altere para a URL de destino desejada
            else:
                messages.error(request, "Credenciais inválidas.")
        else:
            messages.error(request, "Por favor, corrija os erros abaixo.")
    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('principal')