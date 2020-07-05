from django.shortcuts import render
from .forms import MapForm
from .models import Map
from stores.models import Visiting, Store
from django.http import HttpResponse
from django.core.checks import messages
from django.core import serializers

# Create your views here.
# def index(request):
#     return render(request, 'maps/index.html')


def map(request):
    return render(request, 'maps/map.html')


def map1(request):
    return render(request, 'maps/map1.html')


def test(request):
    return render(request, 'maps/test.html')


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


def json(request):
    maps = list(Map.objects.all())
    map_json = serializers.serialize('json', maps, use_natural_foreign_keys=True)
    return HttpResponse(map_json, content_type='application/json')


def index(request):
    all_cnt = Visiting.objects.count()
    print("all_cnt::::", all_cnt)
    stores = Store.objects.all()
    # 날짜 데이터 모아오기
    visitings = Visiting.objects.all()
    visiting_dates = [visiting.visiting_time.date() for visiting in visitings]
    visiting_dates = set(visiting_dates)
    visiting_dates = sorted(visiting_dates)

    visitings_date_cnt ={}
    for date in visiting_dates:
        visiting_list = [visiting for visiting in visitings if visiting.visiting_time.date() == date]
        cnt = len(visiting_list)
        visitings_date_cnt[date] = cnt

    context = {
        'all_cnt': all_cnt,
        'visitings_date_cnt': visitings_date_cnt,
        'stores': stores,
    }
    return render(request, 'maps/index.html', context)


def about(request):
    return render(request, 'maps/about.html')


def about_user(request):
    return render(request, 'maps/about_user.html')


def about_partner(request):
    return render(request, 'maps/about_partner.html')
