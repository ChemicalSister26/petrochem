from django import forms
from .models import *

class Addfeedback(forms.Form):
    title = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    is_published = forms.BooleanField()
    postsfeed = forms.ModelChoiceField(queryset=Basicchem.objects.all())