from django.shortcuts import render
from . import forms

# Create your views here.
def signup(request):
    form = forms.CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)