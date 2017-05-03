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

# class SearchForm(forms.Form):
#     your_name = forms.CharField(label='Your name', max_length=100)