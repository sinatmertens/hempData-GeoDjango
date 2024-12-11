# hempdata/views.py
from django.shortcuts import render, redirect
from .models import Plot, HistoricalData
from .forms import (HistoricalDataForm, SoilPreparationForm, FertilizationForm, SeedingForm, TopCutForm,
                    WeedControlMechanicForm, WeedControlChemicalForm, ConditioningForm, BailingForm, HarvestForm,
                    PlantCharacteristicsBaseForm, SoilSampleForm)
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
    if request.method == 'POST':
        form = HistoricalDataForm(request.POST)

        if form.is_valid():
            form.save()
            # Display success message
            messages.success(request, "Daten wurden erfolgreich hinzugefügt.")
            # Render a new form after successful submission
            return render(request, 'hempdata/historical_data_form.html', {
                'form': HistoricalDataForm(),
                'plots_geojson': serialize('geojson', Plot.objects.all(), geometry_field='location',
                                           fields=('id', 'name')),
                'plots': Plot.objects.all(),  # Pass all plots for the dropdown
                'redirect': True,  # Trigger für JavaScript

            })
    else:
        form = HistoricalDataForm()

    # Serialize Plot objects to GeoJSON
    plots_geojson = serialize('geojson', Plot.objects.all(), geometry_field='location', fields=('id', 'name'))
    plots = Plot.objects.all().order_by('name')  # Fetch all plots

    return render(request, 'hempdata/historical_data_form.html', {
        'form': form,
        'plots': plots,  # Pass the plots to the template
        'plots_geojson': plots_geojson,
    })


def create_soil_preparation(request):
    if request.method == 'POST':
        form = SoilPreparationForm(request.POST)
        if form.is_valid():
            form.save()
            # Display success message
            messages.success(request, "Bodenvorbereitungsdaten wurden erfolgreich hinzugefügt.")
            # Render a new form after successful submission, passing GeoJSON and plot data
            return render(request, 'hempdata/soil_preparation_form.html', {
                'form': SoilPreparationForm(),  # Show a new empty form
                'plots_geojson': serialize('geojson', Plot.objects.all(), geometry_field='location',
                                           fields=('id', 'name')),
                'plots': Plot.objects.all().order_by('name'),
                'redirect': True,
            })
    else:
        form = SoilPreparationForm()

    # Serialize Plot objects to GeoJSON
    plots_geojson = serialize('geojson', Plot.objects.all(), geometry_field='location', fields=('id', 'name'))
    plots = Plot.objects.all().order_by('name')  # Fetch all plots

    return render(request, 'hempdata/soil_preparation_form.html', {
        'form': form,
        'plots': plots,  # Pass the plots to the template
        'plots_geojson': plots_geojson,
    })


def create_fertilization(request):
    if request.method == 'POST':
        form = FertilizationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Düngungsdaten wurden erfolgreich hinzugefügt.")
            return render(request, 'hempdata/fertilization_form.html', {
                'form': FertilizationForm(),
                'plots_geojson': serialize('geojson', Plot.objects.all().order_by('name'), geometry_field='location',
                                           fields=('id', 'name')),
                'plots': Plot.objects.all().order_by('name'),
                'redirect': True,
            })
        else:
            # If the form is invalid, re-render the form with error messages
            messages.error(request, "Es gab einen Fehler beim Speichern der Daten. Bitte prüfen Sie die Eingaben.")
            return render(request, 'hempdata/fertilization_form.html', {
                'form': form,
            })
    else:
        form = FertilizationForm()

    # Serialize Plot objects to GeoJSON
    plots_geojson = serialize('geojson', Plot.objects.all().order_by('name'), geometry_field='location', fields=('id', 'name'))
    plots = Plot.objects.all().order_by('name')  # Fetch all plots

    return render(request, 'hempdata/fertilization_form.html', {
        'form': form,
        'plots': plots,  # Pass the plots to the template
        'plots_geojson': plots_geojson,
    })


def create_seeding(request):
    if request.method == 'POST':
        form = SeedingForm(request.POST)
        if form.is_valid():
            form.save()
            # Erfolgsmeldung anzeigen
            messages.success(request, "Aussaatdaten wurden erfolgreich hinzugefügt.")
            return render(request, 'hempdata/seeding_form.html', {
                'form': SeedingForm(),
                'plots_geojson': serialize('geojson', Plot.objects.all(), geometry_field='location',
                                           fields=('id', 'name')),
                'redirect': True,  # Trigger für JavaScript
            })
    else:
        form = SeedingForm()

    plots_geojson = serialize(
        'geojson',
        Plot.objects.all(),
        geometry_field='location',
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
                'plots_geojson': serialize('geojson', Plot.objects.all(), geometry_field='location',
                                           fields=('id', 'name')),
            })
    else:
        form = TopCutForm()

    plots_geojson = serialize(
        'geojson',
        Plot.objects.all(),
        geometry_field='location',
        fields=('id', 'name')
    )

    return render(request, 'hempdata/topcut_form.html', {
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
                'plots_geojson': serialize('geojson', Plot.objects.all(), geometry_field='location',
                                           fields=('id', 'name')),
            })
    else:
        form = WeedControlMechanicForm()

    plots_geojson = serialize(
        'geojson',
        Plot.objects.all(),
        geometry_field='location',
        fields=('id', 'name')
    )

    return render(request, 'hempdata/weedcontrol_mechanic_form.html', {
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
                'plots_geojson': serialize('geojson', Plot.objects.all(), geometry_field='location',
                                           fields=('id', 'name')),
            })
    else:
        form = WeedControlChemicalForm()

    plots_geojson = serialize(
        'geojson',
        Plot.objects.all(),
        geometry_field='location',
        fields=('id', 'name')
    )

    return render(request, 'hempdata/weedcontrol_chemical_form.html', {
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
                'plots_geojson': serialize('geojson', Plot.objects.all(), geometry_field='location',
                                           fields=('id', 'name')),
            })
    else:
        form = HarvestForm()

    plots_geojson = serialize(
        'geojson',
        Plot.objects.all(),
        geometry_field='location',
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
                'plots_geojson': serialize('geojson', Plot.objects.all(), geometry_field='location',
                                           fields=('id', 'name')),
            })
    else:
        form = ConditioningForm()

    plots_geojson = serialize(
        'geojson',
        Plot.objects.all(),
        geometry_field='location',
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
                'plots_geojson': serialize('geojson', Plot.objects.all(), geometry_field='location',
                                           fields=('id', 'name')),
            })
    else:
        form = BailingForm()

    plots_geojson = serialize(
        'geojson',
        Plot.objects.all(),
        geometry_field='location',
        fields=('id', 'name')
    )

    return render(request, 'hempdata/bailing_form.html', {
        'form': form,
        'plots_geojson': plots_geojson,
    })


def create_plantcharacteristicsbase(request):
    if request.method == 'POST':
        form = PlantCharacteristicsBaseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Pflanzenmerkmalsdaten wurden erfolgreich hinzugefügt.")
            return render(request, 'hempdata/plantcharacteristics_base_form.html', {
                'form': PlantCharacteristicsBaseForm(),
                'plots_geojson': serialize('geojson', Plot.objects.all(), geometry_field='location',
                                           fields=('id', 'name')),
            })
    else:
        form = PlantCharacteristicsBaseForm()

    plots_geojson = serialize(
        'geojson',
        Plot.objects.all(),
        geometry_field='location',
        fields=('id', 'name')
    )

    return render(request, 'hempdata/plantcharacteristics_base_form.html', {
        'form': form,
        'plots_geojson': plots_geojson,
    })


def create_soilsample(request):
    if request.method == 'POST':
        form = SoilSampleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Bodenprobe wurden erfolgreich hinzugefügt.")
            return render(request, 'hempdata/soilsample_form.html', {
                'form': SoilSampleForm(),
                'plots_geojson': serialize('geojson', Plot.objects.all(), geometry_field='location',
                                           fields=('id', 'name')),
            })
    else:
        form = SoilSampleForm()

    plots_geojson = serialize(
        'geojson',
        Plot.objects.all(),
        geometry_field='location',
        fields=('id', 'name')
    )

    return render(request, 'hempdata/soilsample_form.html', {
        'form': form,
        'plots_geojson': plots_geojson,
    })

