from django import forms
from .models import *

class Addfeedback(forms.Form):
    title = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Text')
    is_published = forms.BooleanField(label='Feedback', required=False, initial=True)
    postsfeed = forms.ModelChoiceField(queryset=Basicchem.objects.all(), label='Select a theme', empty_label='a theme is not chosen')