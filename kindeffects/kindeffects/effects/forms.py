from django import forms
from .models import Store, Partner, Map

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'


class MapForm(forms.ModelForm):
    class Meta:
        model = Map
        fields = '__all__'
