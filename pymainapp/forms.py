from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = '__all__'

    widgets = {
        'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Name',
            'style': 'padding: 20px; border: 2px solid #ccc; border-radius: 4px;'
        }),
        'email': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Email',
            'style': 'padding: 10px; border: 1px solid #ccc; border-radius: 4px;'
        }),
        'phone': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your phone',
            'style': 'padding: 10px; border: 1px solid #ccc; border-radius: 4px;'
        }),
        'service': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Select',
            'style': 'padding: 10px; border: 1px solid #ccc; border-radius: 4px;'
        }),
        'message': forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 1,
            'placeholder': 'Message',
            'style': 'padding: 10px; border: 1px solid #ccc; border-radius: 4px;'
        }),
    }



