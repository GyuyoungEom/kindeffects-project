from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'informs/index.html')


def user(request):
    return render(request,'informs/user.html')


def boss(request):
    return render(request,'informs/boss.html')