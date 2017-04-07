from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('upload',)
        widgets = {
            'upload': forms.FileInput(
                attrs={'id': 'fileinput', 'required': True, 'name':'pdf', 'placeholder': 'Say something...'}
            ),
        }