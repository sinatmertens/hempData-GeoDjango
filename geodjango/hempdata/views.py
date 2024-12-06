# hempdata/views.py
from django.shortcuts import render, redirect
from .models import Plot, HistoricalData
from .forms import (HistoricalDataForm, SoilPreparationForm, FertilizationForm, SeedingForm, TopCutForm,
                    WeedControlMechanicForm, WeedControlChemicalForm, ConditioningForm, BailingForm, HarvestForm)
from django.core.serializers import serialize
from django.contrib import messages
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
    """
    Handles the creation of historical data without redirecting.
    """
    if request.method == 'POST':
        form = HistoricalDataForm(request.POST)
        if form.is_valid():
            form.save()
            # Display success message
            messages.success(request, "Daten wurden erfolgreich hinzugefügt.")
            # Render a new form after successful submission
            return render(request, 'hempdata/historical_data_form.html', {
                'form': HistoricalDataForm(),
                'plots_geojson': serialize('geojson', Plot.objects.all(), geometry_field='geometry',
                                           fields=('id', 'name')),
            })
    else:
        form = HistoricalDataForm()

    # Serialize Plot objects to GeoJSON
    plots_geojson = serialize(
        'geojson',
        Plot.objects.all(),
        geometry_field='geometry',
        fields=('id', 'name')
    )

    return render(request, 'hempdata/historical_data_form.html', {
        'form': form,
        'plots_geojson': plots_geojson,
    })


def create_soil_preparation(request):
    if request.method == 'POST':
        form = SoilPreparationForm(request.POST)
        if form.is_valid():
            form.save()
            # Erfolgsmeldung anzeigen
            messages.success(request, "Bodenvorbereitungsdaten wurden erfolgreich hinzugefügt.")
            return render(request, 'hempdata/soil_preparation_form.html', {
                'form': SoilPreparationForm(),  # Neues Formular anzeigen
                'plots_geojson': serialize('geojson', Plot.objects.all(), geometry_field='geometry',
                                           fields=('id', 'name')),
                'redirect': True,  # Trigger für JavaScript
            })
    else:
        form = SoilPreparationForm()

    plots_geojson = serialize(
        'geojson',
        Plot.objects.all(),
        geometry_field='geometry',
        fields=('id', 'name')
    )

    return render(request, 'hempdata/soil_preparation_form.html', {
        'form': form,
        'plots_geojson': plots_geojson,
    })

#
# def create_fertilization(request):
#     if request.method == 'POST':
#         form = FertilizationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Düngungsdaten wurden erfolgreich hinzugefügt.")
#             return render(request, 'hempdata/fertilization_form.html', {
#                 'form': FertilizationForm(),
#                 'plots_geojson': serialize('geojson', Plot.objects.all(), geometry_field='geometry',
#                                            fields=('id', 'name')),
#             })
#     else:
#         form = FertilizationForm()
#
#     plots_geojson = serialize(
#         'geojson',
#         Plot.objects.all(),
#         geometry_field='geometry',
#         fields=('id', 'name')
#     )
#
#     return render(request, 'hempdata/fertilization_form.html', {
#         'form': form,
#         'plots_geojson': plots_geojson,
#     })


def create_seeding(request):
    if request.method == 'POST':
        form = SeedingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Aussaatdaten wurden erfolgreich hinzugefügt.")
            return render(request, 'hempdata/seeding_form.html', {
                'form': SeedingForm(),
                'plots_geojson': serialize('geojson', Plot.objects.all(), geometry_field='geometry',
                                           fields=('id', 'name')),
            })
    else:
        form = SeedingForm()

    plots_geojson = serialize(
        'geojson',
        Plot.objects.all(),
        geometry_field='geometry',
        fields=('id', 'name')
    )

    return render(request, 'hempdata/seeding_form.html', {
        'form': form,
        'plots_geojson': plots_geojson,
    })


def create_top_cut(request):
    if request.method == 'POST':
        form = TopCutForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Kopfschnittdaten wurden erfolgreich hinzugefügt.")
            return render(request, 'hempdata/topcut_form.html', {
                'form': TopCutForm(),
                'plots_geojson': serialize('geojson', Plot.objects.all(), geometry_field='geometry',
                                           fields=('id', 'name')),
            })
    else:
        form = TopCutForm()

    plots_geojson = serialize(
        'geojson',
        Plot.objects.all(),
        geometry_field='geometry',
        fields=('id', 'name')
    )

    return render(request, 'hempdata/top_cut_form.html', {
        'form': form,
        'plots_geojson': plots_geojson,
    })


def create_weed_control_mechanic(request):
    if request.method == 'POST':
        form = WeedControlMechanicForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mechanische Unkrautbekämpfungsdaten wurden erfolgreich hinzugefügt.")
            return render(request, 'hempdata/weedcontrol_mechanic_form.html', {
                'form': WeedControlMechanicForm(),
                'plots_geojson': serialize('geojson', Plot.objects.all(), geometry_field='geometry',
                                           fields=('id', 'name')),
            })
    else:
        form = WeedControlMechanicForm()

    plots_geojson = serialize(
        'geojson',
        Plot.objects.all(),
        geometry_field='geometry',
        fields=('id', 'name')
    )

    return render(request, 'hempdata/weed_control_mechanic_form.html', {
        'form': form,
        'plots_geojson': plots_geojson,
    })


def create_weed_control_chemical(request):
    if request.method == 'POST':
        form = WeedControlChemicalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Chemische Unkrautbekämpfungsdaten wurden erfolgreich hinzugefügt.")
            return render(request, 'hempdata/weedcontrol_chemical_form.html', {
                'form': WeedControlChemicalForm(),
                'plots_geojson': serialize('geojson', Plot.objects.all(), geometry_field='geometry',
                                           fields=('id', 'name')),
            })
    else:
        form = WeedControlChemicalForm()

    plots_geojson = serialize(
        'geojson',
        Plot.objects.all(),
        geometry_field='geometry',
        fields=('id', 'name')
    )

    return render(request, 'hempdata/weed_control_chemical_form.html', {
        'form': form,
        'plots_geojson': plots_geojson,
    })


def create_harvest(request):
    if request.method == 'POST':
        form = HarvestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Erntedaten wurden erfolgreich hinzugefügt.")
            return render(request, 'hempdata/harvest_form.html', {
                'form': HarvestForm(),
                'plots_geojson': serialize('geojson', Plot.objects.all(), geometry_field='geometry',
                                           fields=('id', 'name')),
            })
    else:
        form = HarvestForm()

    plots_geojson = serialize(
        'geojson',
        Plot.objects.all(),
        geometry_field='geometry',
        fields=('id', 'name')
    )

    return render(request, 'hempdata/harvest_form.html', {
        'form': form,
        'plots_geojson': plots_geojson,
    })


def create_conditioning(request):
    if request.method == 'POST':
        form = ConditioningForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Aufbereitungsdaten wurden erfolgreich hinzugefügt.")
            return render(request, 'hempdata/conditioning_form.html', {
                'form': ConditioningForm(),
                'plots_geojson': serialize('geojson', Plot.objects.all(), geometry_field='geometry',
                                           fields=('id', 'name')),
            })
    else:
        form = ConditioningForm()

    plots_geojson = serialize(
        'geojson',
        Plot.objects.all(),
        geometry_field='geometry',
        fields=('id', 'name')
    )

    return render(request, 'hempdata/conditioning_form.html', {
        'form': form,
        'plots_geojson': plots_geojson,
    })


def create_bailing(request):
    if request.method == 'POST':
        form = BailingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ballengewichtsdaten wurden erfolgreich hinzugefügt.")
            return render(request, 'hempdata/bailing_form.html', {
                'form': BailingForm(),
                'plots_geojson': serialize('geojson', Plot.objects.all(), geometry_field='geometry',
                                           fields=('id', 'name')),
            })
    else:
        form = BailingForm()

    plots_geojson = serialize(
        'geojson',
        Plot.objects.all(),
        geometry_field='geometry',
        fields=('id', 'name')
    )

    return render(request, 'hempdata/bailing_form.html', {
        'form': form,
        'plots_geojson': plots_geojson,
    })
