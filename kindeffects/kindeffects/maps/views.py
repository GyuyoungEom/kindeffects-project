from django.shortcuts import render
from .forms import MapForm
from django.http import HttpResponse
from django.core.checks import messages

# Create your views here.
def index(request):
    return render(request, 'maps/index.html')


def map(request):
    return render(request, 'maps/map.html')


def test1(request):
    return render(request, 'maps/test1.html')


def test2(request):
    return render(request, 'maps/test2.html')

def ajtest(request):
    if request.method == 'POST':
        form = MapForm(request.POST)
        print(form.data)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            # messages.success(request, f"Success!!")
            return HttpResponse('ok')
    # if request.method == 'POST':
    #     model = MyModel()
    #     model.value = request.POST['data']
    #     model.user = request.user
    #     model.save()
    # else:
        # messages.success(request, f"Error")
    return HttpResponse('error')