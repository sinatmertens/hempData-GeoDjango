# hempdata/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.navigation, name='navigation'),
    path('historical-data/new/', views.create_historical_data, name='historical_data_form'),
    #path('formular1/', views.formular1, name='formular1'),
    #path('formular2/', views.formular2, name='formular2'),
    #path('formular3/', views.formular3, name='formular3'),
    #path('map/', views.map_view, name='map_view'),
    #path('add-preparation-data/', views.add_preparation_data, name='add_preparation_data'),
    #path('preparation-data-success/', views.preparation_data_success, name='preparation_data_success'), # Success page URL

]
