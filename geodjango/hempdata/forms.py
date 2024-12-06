from django import forms
from .models import (
    HistoricalData, SoilPreparation, Fertilization,
    Seeding, TopCut, WeedControlMechanic, WeedControlChemical,
    Harvest, Conditioning, Bailing, WeatherStation, WeatherData,
    PlantCharacteristicsTop, PlantCharacteristicsBase, SoilData
)


class HistoricalDataForm(forms.ModelForm):
    class Meta:
        model = HistoricalData
        fields = ['plot', 'previous_crop1', 'previous_crop2']

    def clean_plot(self):
        plot = self.cleaned_data['plot']
        if HistoricalData.objects.filter(plot=plot).exists():
            raise forms.ValidationError("Für diesen Schlag wurden bereits historische Daten eingegeben.")
        return plot


class SoilPreparationForm(forms.ModelForm):
    class Meta:
        model = SoilPreparation
        fields = ['completed', 'plot', 'intensity', 'type']

    def clean_plot(self):
        plot = self.cleaned_data['plot']
        if SoilPreparation.objects.filter(plot=plot).exists():
            raise forms.ValidationError("Für diesen Schlag wurden bereits Bodenvorbereitungsdaten eingegeben.")
        return plot


class FertilizationForm(forms.ModelForm):
    class Meta:
        model = Fertilization
        fields = ['plot', 'completed', 'fertilizer', 'amount', 'created_at']

    def clean_plot(self):
        plot = self.cleaned_data['plot']
        if Fertilization.objects.filter(plot=plot, created_at=self.cleaned_data['created_at']).exists():
            raise forms.ValidationError("Für diesen Schlag wurde bereits eine Düngung an diesem Datum eingetragen.")
        return plot


class SeedingForm(forms.ModelForm):
    class Meta:
        model = Seeding
        fields = ['plot', 'variety', 'seeding_rate', 'seedbed_width', 'thousand_grain_weight']

    def clean_plot(self):
        plot = self.cleaned_data['plot']
        if Seeding.objects.filter(plot=plot).exists():
            raise forms.ValidationError("Für diesen Schlag wurde bereits eine Aussaat eingetragen.")
        return plot


class TopCutForm(forms.ModelForm):
    class Meta:
        model = TopCut
        fields = ['plot', 'cutting_height']

    def clean_plot(self):
        plot = self.cleaned_data['plot']
        if TopCut.objects.filter(plot=plot).exists():
            raise forms.ValidationError("Für diesen Schlag wurde bereits ein Kopfschnitt eingetragen.")
        return plot


class WeedControlMechanicForm(forms.ModelForm):
    class Meta:
        model = WeedControlMechanic
        fields = ['plot', 'hacken', 'striegeln', 'rollen', 'emergence']


class WeedControlChemicalForm(forms.ModelForm):
    class Meta:
        model = WeedControlChemical
        fields = ['plot', 'substance', 'amount']


class HarvestForm(forms.ModelForm):
    class Meta:
        model = Harvest
        fields = ['plot', 'procedure']

    def clean_plot(self):
        plot = self.cleaned_data['plot']
        if Harvest.objects.filter(plot=plot).exists():
            raise forms.ValidationError("Für diesen Schlag wurde bereits eine Ernte eingetragen.")
        return plot


class ConditioningForm(forms.ModelForm):
    class Meta:
        model = Conditioning
        fields = ['plot', 'procedure']


class BailingForm(forms.ModelForm):
    class Meta:
        model = Bailing
        fields = ['plot', 'weight']

    def clean_plot(self):
        plot = self.cleaned_data['plot']
        if Bailing.objects.filter(plot=plot).exists():
            raise forms.ValidationError("Für diesen Schlag wurde bereits ein Ballen eingetragen.")
        return plot