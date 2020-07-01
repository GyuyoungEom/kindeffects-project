from django.shortcuts import render, redirect
from .models import Store
from .forms import StoreForm
from django.contrib.auth.decorators import login_required

import qrcode
import qrcode.image.svg
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

@login_required
def update(request):
    print(request.user.store_id)
    store = Store.objects.get(pk=request.user.store_id)
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
    return redirect('accounts:update')




def detail(request, store_pk):
    store = get_object_or_404(Store, pk=store_pk)
    context = {
        'store': store,
    }
    return render(request, 'stores/store_detail.html', context)

# qr이 인식되면 visit_time이 저장됨.
def visiting(request, store_pk):
    store = get_object_or_404(Store, pk=store_pk)
    visiting = Visiting.objects.create()
    visiting.store = store
    visiting.save()
    return redirect('stores:detail', store_pk)

# 로그인 조건을 추가해야 함.
def mypage(request, store_pk):
    store = get_object_or_404(Store, pk=store_pk)
    context = {
        'store': store,
    }
    return render(request, 'stores/store_mypage.html', context)

# 수퍼유저 로그인 조건을 추가해야 함.
def qr(request, store_pk):
    domain = "http://www.dreamtree.site"
    store_url = f"{domain}/stores/qr/{store_pk}/" 

        # svg 로 저장
    method = 'basic'
    if method == 'basic':
        # Simple factory, just a set of rects.
        factory = qrcode.image.svg.SvgImage
    elif method == 'fragment':
        # Fragment factory (also just a set of rects)
        factory = qrcode.image.svg.SvgFragmentImage
    else:
        # Combined path factory, fixes white space that may occur when zooming
        factory = qrcode.image.svg.SvgPathImage

    svg = qrcode.make(store_url, image_factory=factory)
    print(svg)

    svg.save(f"qr_{store_pk}.svg")

    # qr = Qr.objects.create()
    # qr.svg = svg
    
    # QR 코드 저장하는 것 보다, 필요시점에 렌더링하는 것으로 변경을 추천
    
    return redirect('stores:index')
