from django.urls import path
from . import views

app_name = 'maps'

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map, name='map'),
    path('map1/', views.map1, name='map1'),
    path('test/', views.test, name='test'),
    path('test1/', views.test1, name='test1'),
    path('test2/', views.test2, name='test2'),
    path('ajtest/', views.ajtest, name='ajtest'),
    path('json/', views.json, name='json'),
    path('about/', views.about, name='about'),
    path('about_user/', views.about_user, name='about_user'),
    path('about_partner/', views.about_partner, name='about_partner'),
]
