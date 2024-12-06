# hempdata/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.navigation, name='navigation'),
    path('historical-data/new/', views.create_historical_data, name='historical_data_form'),
    path('soil-preparation/new/', views.create_soil_preparation, name='soil_preparation_form'),
    path('weed-control-mechanic/', views.create_weed_control_mechanic, name='create_weed_control_mechanic'),
    path('weed-control-chemical/', views.create_weed_control_chemical, name='create_weed_control_chemical'),
    path('harvest/', views.create_harvest, name='create_harvest'),
    #path('fertilization/', views.create_fertilization, name='create_fertilization'),
    path('seeding/', views.create_seeding, name='create_seeding'),
    path('top-cut/', views.create_top_cut, name='create_top_cut'),
    path('conditioning/', views.create_conditioning, name='create_conditioning'),
    path('bailing/', views.create_bailing, name='create_bailing'),

]
