# hempdata/views.py
from django.shortcuts import render, redirect
from .forms import HistoricalDataForm
from django.core.serializers import serialize
from django.http import HttpResponse
import json


def navigation(request):
    if request.method == 'POST':
        form = HistoricalDataForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'hempdata/navigation.html', {'form': HistoricalDataForm(), 'success': True})
    else:
        form = HistoricalDataForm()
    return render(request, 'hempdata/navigation.html', {'form': form})


# def map_view(request):
#    fields_geojson = serialize('geojson', Field.objects.all(), geometry_field='location')
#    plots_geojson = serialize('geojson', Plot.objects.all(), geometry_field='location')

#    context = {
#        'fields_geojson': fields_geojson,
#        'plots_geojson': plots_geojson,
#    }
#    return render(request, 'hempdata/map_view.html', context)

def create_historical_data(request):
    if request.method == 'POST':
        form = HistoricalDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('navigation')  # Zurück zur Navigation nach dem Speichern
    else:
        form = HistoricalDataForm()
    return render(request, 'hempdata/historical_data_form.html', {'form': form})
