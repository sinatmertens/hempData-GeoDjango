# hempdata/views.py
from django.shortcuts import render, redirect
from .models import Plot, HistoricalData
from .forms import HistoricalDataForm
from django.core.serializers import serialize
from .models import Plot
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





def create_historical_data(request):
    # Handle form submission
    if request.method == 'POST':
        form = HistoricalDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('navigation')  # Redirect to another page after saving
    else:
        form = HistoricalDataForm()

    # Serialize Plot objects to GeoJSON
    plots_geojson = serialize(
        'geojson',
        Plot.objects.all(),
        geometry_field='geometry',  # Ensure 'geometry' is the spatial field
        fields=('id', 'name')
    )

    return render(request, 'hempdata/historical_data_form.html', {
        'form': form,
        'plots_geojson': plots_geojson,
    })