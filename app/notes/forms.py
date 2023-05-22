from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'text_note', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text_note': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class UpdateNoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'text_note', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text_note': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

