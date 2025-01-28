from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Evento, Participacao
from .forms import EventoForm  

def principal(request):
    template = loader.get_template('principal.html')
    return HttpResponse(template.render())

@login_required
def meus_eventos(request):
    participacoes = Participacao.objects.filter(usuario=request.user)
    
    # Extrair os eventos a partir das participações
    eventos = [participacao.evento for participacao in participacoes]
    return render(request, 'meus_eventos.html', {'eventos': eventos})

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
                return redirect('principal')  
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

#CRUD
#Create
@login_required
def criar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.organizador = request.user  # Define o usuário logado como organizador
            evento.save()

            # Adiciona automaticamente o organizador como participante
            Participacao.objects.create(usuario=request.user, evento=evento, eh_organizador=True)
            
            messages.success(request, 'Evento criado com sucesso!')
            return redirect('meus_eventos') 
    else:
        form = EventoForm()
    
    return render(request, 'criar_evento.html', {'form': form})

#Read
def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'listar_eventos.html', {'eventos': eventos})

def detalhar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    return render(request, 'detalhar_evento.html', {'evento': evento})

#Update
@login_required
def editar_evento(request, id):
    evento = get_object_or_404(Evento, id=id, organizador=request.user)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evento atualizado com sucesso!')
            return redirect('detalhar_evento', id=evento.id)
    else:
        form = EventoForm(instance=evento)
    
    return render(request, 'editar_evento.html', {'form': form, 'evento': evento})

#Delete
@login_required
def deletar_evento(request, id):
    evento = get_object_or_404(Evento, id=id, organizador=request.user)
    if request.method == 'POST':
        evento.delete()
        messages.success(request, 'Evento deletado com sucesso!')
        return redirect('meus_eventos') 
    return render(request, 'deletar_evento.html', {'evento': evento})

@login_required
def inscricao_em_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    if not Participacao.objects.filter(evento=evento, usuario=request.user).exists():
        # Se o usuário já estiver inscrito, não permita a inscrição
        messages.info(request, 'Você já está inscrito neste evento.')
        return redirect('detalhar_evento', id=evento.id)

    Participacao.objects.create(evento=evento, usuario=request.user)
    messages.success(request, 'Você se inscreveu com sucesso no evento!')
    return redirect('detalhar_evento', id=evento.id)

@login_required
def cancelar_inscricao(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if Participacao.objects.filter(evento=evento, usuario=request.user).exists():
        evento.participantes.remove(request.user)
        messages.success(request, f'Você cancelou sua inscrição no evento com sucesso. "{evento.titulo}".')

    return redirect('detalhar_evento', evento_id=evento.id)