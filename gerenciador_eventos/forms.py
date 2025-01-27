from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

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