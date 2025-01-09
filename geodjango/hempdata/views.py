# hempdata/views.py
from django.shortcuts import render, redirect
from django.core.serializers import serialize
from django.contrib import messages
from .models import (PlantCharacteristicsBase, SoilSample, Plot, Bailing, TopCut, Harvest, Conditioning, HistoricalData, SoilPreparation, Fertilization, Seeding, PlotParts, WeedControlMechanic, WeedControlChemical)
from .forms import (
    HistoricalDataForm, TopCutForm, WeedControlMechanicForm,
    WeedControlChemicalForm, ConditioningForm, BailingForm,
    HarvestForm, PlantCharacteristicsBaseForm, SoilSampleForm, SoilPreparationForm, FertilizationForm, SeedingForm)



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
            messages.success(request, "Daten wurden erfolgreich hinzugefügt.")
            return redirect('historical_data_form')

    else:
        form = HistoricalDataForm()

    # Daten für die Darstellung abrufen
    plots_geojson = serialize('geojson', Plot.objects.all(), geometry_field='location', fields=('id', 'name'))
    plots = Plot.objects.all().order_by('name')
    historical_data = HistoricalData.objects.all().order_by('created_at')  # Historische Daten laden

    return render(request, 'hempdata/historical_data_form.html', {
        'form': form,
        'plots': plots,  # Plots für das Dropdown
        'plots_geojson': plots_geojson,  # GeoJSON-Daten für die Karte
        'historical_data': historical_data,  # Historische Daten für die Tabelle
    })


def create_soil_preparation(request):
    if request.method == 'POST':
        form = SoilPreparationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Bodenvorbereitungsdaten wurden erfolgreich hinzugefügt.")
            return redirect('soil_preparation_form')

    else:
        form = SoilPreparationForm()

    # Fetch existing soil preparation data
    soil_preparation_data = SoilPreparation.objects.all().order_by('plot')
    plots_geojson = serialize('geojson', Plot.objects.all(), geometry_field='location', fields=('id', 'name'))
    plots = Plot.objects.all().order_by('name')

    return render(request, 'hempdata/soil_preparation_form.html', {
        'form': form,
        'plots': plots,
        'plots_geojson': plots_geojson,
        'soil_preparation_data': soil_preparation_data,
    })


def create_fertilization(request):
    if request.method == 'POST':
        form = FertilizationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Düngungsdaten wurden erfolgreich hinzugefügt.")
            # Redirect, um die Seite neu zu laden und das Formular zu leeren
            return redirect('fertilization_form')
        else:
            messages.error(request, "Es gab einen Fehler beim Speichern der Daten. Bitte prüfen Sie die Eingaben.")

    else:
        form = FertilizationForm()

    # Bestehende Düngungsdaten abrufen
    fertilization_data = Fertilization.objects.all().order_by('plot')
    plots_geojson = serialize('geojson', Plot.objects.all().order_by('name'), geometry_field='location',
                              fields=('id', 'name'))
    plots = Plot.objects.all().order_by('name')

    return render(request, 'hempdata/fertilization_form.html', {
        'form': form,
        'plots': plots,
        'plots_geojson': plots_geojson,
        'fertilization_data': fertilization_data,  # Bestehende Daten für die Tabelle
    })


def create_seeding(request):
    if request.method == 'POST':
        form = SeedingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Aussaatdaten wurden erfolgreich hinzugefügt.")
            return redirect('seeding_form')  # Redirect to reload the page and refresh the table

    else:
        form = SeedingForm()

    # Fetch existing seeding data
    seeding_data = Seeding.objects.all().order_by('plot')
    plots_geojson = serialize('geojson', Plot.objects.all(), geometry_field='location', fields=('id', 'name'))

    return render(request, 'hempdata/seeding_form.html', {
        'form': form,
        'plots_geojson': plots_geojson,
        'seeding_data': seeding_data,  # Pass existing seeding data to the template
    })


def create_top_cut(request):
    if request.method == 'POST':
        form = TopCutForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Kopfschnittdaten wurden erfolgreich hinzugefügt.")
            return redirect('topcut_form')  # Redirect to reload and refresh the table

    else:
        form = TopCutForm()

    # Fetch existing top-cut data
    top_cut_data = TopCut.objects.all().order_by('plot')
    plots_geojson = serialize(
        'geojson',
        Plot.objects.all(),
        geometry_field='location',
        fields=('id', 'name')
    )

    return render(request, 'hempdata/topcut_form.html', {
        'form': form,
        'plots_geojson': plots_geojson,
        'top_cut_data': top_cut_data,  # Pass top-cut data to the template
    })

def create_weed_control_mechanic(request):
    if request.method == 'POST':
        form = WeedControlMechanicForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mechanische Unkrautbekämpfungsdaten wurden erfolgreich hinzugefügt.")
            return redirect('weedcontrol_mechanic_form')  # Redirect to reload and refresh the table

    else:
        form = WeedControlMechanicForm()

    # Fetch existing weed control data
    weed_control_data = WeedControlMechanic.objects.all().order_by('plot')
    plots_geojson = serialize(
        'geojson',
        Plot.objects.all(),
        geometry_field='location',
        fields=('id', 'name')
    )

    return render(request, 'hempdata/weedcontrol_mechanic_form.html', {
        'form': form,
        'plots_geojson': plots_geojson,
        'weed_control_data': weed_control_data,  # Pass weed control data to the template
    })

def create_weed_control_chemical(request):
    if request.method == 'POST':
        form = WeedControlChemicalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Chemische Unkrautbekämpfungsdaten wurden erfolgreich hinzugefügt.")
            return redirect('weedcontrol_chemical_form')  # Redirect to reload and refresh the table

    else:
        form = WeedControlChemicalForm()

    # Fetch existing chemical weed control data
    weed_control_chemical_data = WeedControlChemical.objects.all().order_by('plot')
    plots_geojson = serialize(
        'geojson',
        Plot.objects.all(),
        geometry_field='location',
        fields=('id', 'name')
    )

    return render(request, 'hempdata/weedcontrol_chemical_form.html', {
        'form': form,
        'plots_geojson': plots_geojson,
        'weed_control_chemical_data': weed_control_chemical_data,  # Pass data to the template
    })

def create_harvest(request):
    if request.method == 'POST':
        form = HarvestForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Erntedaten wurden erfolgreich hinzugefügt.")
                return redirect('harvest_form')  # Redirect to reload and refresh the table
            except ValueError:
                messages.warning(request, "Für diesen Schlag wurde bereits eine Ernte eingetragen.")
        else:
            messages.error(request, "Es gab einen Fehler beim Speichern der Daten. Bitte prüfen Sie die Eingaben.")

    else:
        form = HarvestForm()

    # Fetch existing harvest data
    harvest_data = Harvest.objects.all().order_by('plotpart')
    plots_geojson = serialize(
        'geojson',
        PlotParts.objects.all(),
        geometry_field='location',
        fields=('id')
    )

    return render(request, 'hempdata/harvest_form.html', {
        'form': form,
        'plots_geojson': plots_geojson,
        'harvest_data': harvest_data,  # Pass harvest data to the template
    })

def create_conditioning(request):
    if request.method == 'POST':
        form = ConditioningForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Aufbereitungsdaten wurden erfolgreich hinzugefügt.")
            return redirect('conditioning_form')  # Redirect to reload and refresh the table

    else:
        form = ConditioningForm()

    # Fetch existing conditioning data
    conditioning_data = Conditioning.objects.all().order_by('id')
    plots_geojson = serialize(
        'geojson',
        PlotParts.objects.all(),
        geometry_field='location',
        fields=('id', 'name')
    )

    return render(request, 'hempdata/conditioning_form.html', {
        'form': form,
        'plots_geojson': plots_geojson,
        'conditioning_data': conditioning_data,  # Pass conditioning data to the template
    })

def create_bailing(request):
    if request.method == 'POST':
        form = BailingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ballengewichtsdaten wurden erfolgreich hinzugefügt.")
            return redirect('bailing_form')  # Redirect to reload and refresh the table

    else:
        form = BailingForm()

    # Fetch existing bailing data
    bailing_data = Bailing.objects.all().order_by('plotpart')
    plots_geojson = serialize(
        'geojson',
        PlotParts.objects.all(),
        geometry_field='location',
        fields=('id', 'name')
    )

    return render(request, 'hempdata/bailing_form.html', {
        'form': form,
        'plots_geojson': plots_geojson,
        'bailing_data': bailing_data,  # Pass bailing data to the template
    })

def create_plantcharacteristicsbase(request):
    if request.method == 'POST':
        form = PlantCharacteristicsBaseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Pflanzenmerkmalsdaten wurden erfolgreich hinzugefügt.")
            return redirect('plantcharacteristics_base_form')  # Redirect to reload and refresh the table

    else:
        form = PlantCharacteristicsBaseForm()

    # Fetch existing plant characteristics data
    plant_characteristics_data = PlantCharacteristicsBase.objects.all().order_by('plot')
    plots_geojson = serialize(
        'geojson',
        Plot.objects.all(),
        geometry_field='location',
        fields=('id', 'name')
    )

    return render(request, 'hempdata/plantcharacteristics_base_form.html', {
        'form': form,
        'plots_geojson': plots_geojson,
        'plant_characteristics_data': plant_characteristics_data,  # Pass data to the template
    })

def create_soilsample(request):
    if request.method == 'POST':
        form = SoilSampleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Bodenprobe wurde erfolgreich hinzugefügt.")
            return redirect('soilsample_form')  # Redirect to reload and refresh the table

    else:
        form = SoilSampleForm()

    # Fetch existing soil sample data
    soil_sample_data = SoilSample.objects.all().order_by('plot')
    plots_geojson = serialize(
        'geojson',
        Plot.objects.all(),
        geometry_field='location',
        fields=('id', 'name')
    )

    return render(request, 'hempdata/soilsample_form.html', {
        'form': form,
        'plots_geojson': plots_geojson,
        'soil_sample_data': soil_sample_data,  # Pass soil sample data to the template
    })