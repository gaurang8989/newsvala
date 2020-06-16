from django.urls import path
from.import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('khedut', views.khedut, name='khedut'),
    path('janvajevu', views.janvajevu, name='janvajevu'),
    path('lekh', views.lekh, name='lekh'),
    path('rajkaran', views.rajkaran, name='rajkaran'),
    path('dharmik', views.dharmik, name='dharmik'),
    path('swasthya', views.swasthya, name='swasthya'),
    path('samachar', views.samachar, name='samachar'),
    path('about', views.about, name='about'),
]