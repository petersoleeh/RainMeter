from django import forms
from .models import Raindata

class RainForm(forms.ModelForm):

    class Meta:
        model = Raindata
        fields = ('__all__')
        widgets = {
            'month':forms.TextInput(attrs={'placeholder': 'Month'})
        }
