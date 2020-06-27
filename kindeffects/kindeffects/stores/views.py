from django.shortcuts import render, redirect
from .models import Store
from .forms import StoreForm

# Create your views here.
def index(request):
    stores = Store.objects.all()
    context = {
        'stores' : stores,
    }
    return render(request, 'stores/index.html', context)


def store_new(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stores:index')
    else:
        form = StoreForm()

    context = {
        'form': form,
    }
    return render(request, 'stores/store_new.html', context)
