from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
        help_texts = {
            "username": "",
            "password1": "",
            "password2": "",
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

class ContactoForm(forms.Form):
    email = forms.EmailField(label="Correo electrónico", max_length=100)
    asunto = forms.CharField(label="Asunto", max_length=150)
    mensaje = forms.CharField(label="Mensaje")