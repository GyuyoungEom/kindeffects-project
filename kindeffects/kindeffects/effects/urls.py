from django.urls import path
from . import views

app_name = 'effects'

urlpatterns = [
    path('', views.index, name='index'),
    path('store/new/', views.store_new, name='store_new'),
    path('home/', views.home, name='home'),
]
