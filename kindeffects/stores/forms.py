from django import forms
from .models import Store

class StoreForm(forms.ModelForm):
    open_hour = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type':'time',
            }
        )
    )
    closed_hour = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type':'time',
            }
        )
    )
    num = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type':'tel',
            }
        )
    )
    class Meta:
        model = Store
        fields = '__all__'
