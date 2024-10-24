from django import forms
from .models import EmailTask

class MessageForm(forms.ModelForm):
    class Meta:
        model = EmailTask
        fields = ['emails', 'subject', 'message']

    
