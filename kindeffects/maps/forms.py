from django import forms
from .models import Map

class MapForm(forms.ModelForm):
    class Meta:
        model = Map
        # fields = '__all__'
        fields = ('lat', 'lon', )
