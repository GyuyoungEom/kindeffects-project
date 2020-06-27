from django.urls import path
from . import views

app_name = 'maps'

urlpatterns = [
    path('home/', views.home, name='home'),

]
