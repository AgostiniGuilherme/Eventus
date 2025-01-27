from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Evento


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Usuário ou Email", max_length=254)

    def clean_username(self):
        username_or_email = self.cleaned_data.get('username')

        if '@' in username_or_email:
            try:
                user = User.objects.get(email=username_or_email)
                return user.username 
            except User.DoesNotExist:
                raise forms.ValidationError("Este email não está cadastrado.")
        else:
            return username_or_email
        
class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descricao', 'local', 'data'] 

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o título do evento'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Digite uma descrição para o evento', 'rows': 4}),
            'local': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Informe o local do evento'}),
            'data': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

    def clean_data(self):
        data = self.cleaned_data.get('data')
        if data is None:
            raise forms.ValidationError("Por favor, informe uma data válida para o evento.")
        return data
