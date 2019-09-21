from django import forms
from django.forms import widgets
from webapp.models import STATUS_CHOICES


class RegisterForm(forms.Form):
    author = forms.CharField(max_length=50, required=True, label='Name')
    email = forms.EmailField(required=True, label='Email')
    text = forms.CharField(max_length=3000, required=True, label='Text', widget=widgets.Textarea)
