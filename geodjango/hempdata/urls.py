# hempdata/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.map_view, name='map_view'),
    path('add-preparation-data/', views.add_preparation_data, name='add_preparation_data'),
    path('preparation-data-success/', views.preparation_data_success, name='preparation_data_success'), # Success page URL

]
