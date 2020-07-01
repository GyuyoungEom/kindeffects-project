from django.urls import path
from . import views

app_name = 'stores'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.store_new, name='store_new'),
    path('update/', views.update, name='update'),
    path('<int:store_pk>', views.detail, name='detail'),
    # QR 코드가 인식됨
    path('visiting/<int:store_pk>', views.visiting, name='visiting'),
    # 업체의 MyPage
    path('<int:store_pk>/mypage', views.mypage, name='mypage'),
    # QR 코드 생성
    path('qr/<int:store_pk>', views.qr, name='qr'),
]
