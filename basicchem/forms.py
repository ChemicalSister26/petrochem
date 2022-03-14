from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *

class Addfeedback(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label="category is not chosen"

    class Meta:
        model = Basicchem
        fields = ['title', 'slug', 'content', 'photo', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 68, 'rows': 18}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('length is more than 200 characters')
        return title


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='password1', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='password2', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label='email', widget=forms.EmailInput(attrs={'class': 'form-input'}))


    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')
