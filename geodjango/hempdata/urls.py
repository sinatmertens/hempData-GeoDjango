# hempdata/urls.py
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    #path('hempdata/', include('hempdata.urls')),  # Include app-level URLs
    path('', views.navigation, name='navigation'),
    path('historical-data/new/', views.create_historical_data, name='historical_data_form'),
    path('soil-preparation/new/', views.create_soil_preparation, name='soil_preparation_form'),
    path('weed-control-mechanic/', views.create_weed_control_mechanic, name='weedcontrol_mechanic_form'),
    path('weed-control-chemical/', views.create_weed_control_chemical, name='weedcontrol_chemical_form'),
    path('harvest/', views.create_harvest, name='harvest_form'),
    path('fertilization/', views.create_fertilization, name='fertilization_form'),
    path('seeding/new/', views.create_seeding, name='seeding_form'),
    path('top-cut/', views.create_top_cut, name='topcut_form'),
    path('conditioning/', views.create_conditioning, name='conditioning_form'),
    path('bailing/', views.create_bailing, name='bailing_form'),
    path('soilsample/', views.create_soilsample, name='soilsample_form'),
    path('plant-characteristics-base/', views.create_plantcharacteristicsbase, name='plantcharacteristics_base_form'),

]
