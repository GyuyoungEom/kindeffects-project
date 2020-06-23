from django import forms
from .models import Store, Map

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


# class PartnerForm(forms.ModelForm):
#     class Meta:
#         model = Partner
#         fields = '__all__'


class MapForm(forms.ModelForm):
    class Meta:
        model = Map
        fields = '__all__'
