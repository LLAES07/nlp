from django import forms
from .models import FormSending

class FormSendingForm(forms.ModelForm):
    class Meta:
        model = FormSending
        fields = ['nombre', 'descripcion', 'category']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa tu nombre'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }