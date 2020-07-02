from django.urls import path
from . import views

app_name = 'maps'

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map, name='map'),
    path('test1/', views.test1, name='test1'),
    path('test2/', views.test2, name='test2'),
    path('ajtest/', views.ajtest, name='ajtest'),
]
