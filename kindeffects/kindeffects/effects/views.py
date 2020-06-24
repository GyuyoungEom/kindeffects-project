from django.shortcuts import render, redirect
from .models import Store
from .forms import StoreForm

# Create your views here.
def index(request):
    stores = Store.objects.all()
    context = {
        'stores' : stores,
    }
    return render(request, 'effects/index.html', context)


def store_new(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('effects:index')
    else:
        form = StoreForm()

    context = {
        'form': form,
    }
    return render(request, 'effects/store_new.html', context)


def home(request):
    return render(request, 'effects/home.html')