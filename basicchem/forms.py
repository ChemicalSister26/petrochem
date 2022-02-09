from django import forms
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