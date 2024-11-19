# hempdata/views.py
from django.shortcuts import render, redirect
from django.core.serializers import serialize
from .forms import PreparationDataForm
from .models import Field, Plot
from django.http import HttpResponse
import json

def map_view(request):
    fields_geojson = serialize('geojson', Field.objects.all(), geometry_field='location')
    plots_geojson = serialize('geojson', Plot.objects.all(), geometry_field='location')

    context = {
        'fields_geojson': fields_geojson,
        'plots_geojson': plots_geojson,
    }
    return render(request, 'hempdata/map_view.html', context)

def add_preparation_data(request):
    if request.method == 'POST':
        form = PreparationDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('preparation_data_success')
    else:
        form = PreparationDataForm()

    # Serialize without relying on `fields` and add `id` manually
    plots = Plot.objects.all()
    plots_geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    for plot in plots:
        plots_geojson["features"].append({
            "type": "Feature",
            "geometry": json.loads(plot.location.geojson),
            "properties": {
                "id": plot.id
            }
        })

    return render(request, 'hempdata/add_preparation_data.html', {
        'form': form,
        'plots_geojson': json.dumps(plots_geojson)  # Serialize for the template
    })

def preparation_data_success(request):
    return HttpResponse("Preparation data successfully submitted!")