from django.urls import path
from . import views


app_name='informs'

urlpatterns = [
    path('',views.index,name='index'),
    path('user/',views.user,name='user'),
    path('boss/',views.boss,name='boss'),
]
