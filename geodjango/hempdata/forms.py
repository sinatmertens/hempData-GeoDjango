from django import forms
from .models import (
    HistoricalData, SoilPreparation, Fertilization,
    Seeding, TopCut, WeedControlMechanic, WeedControlChemical,
    Harvest, Conditioning, Bailing, WeatherStation, WeatherData,
    PlantCharacteristicsTop, PlantCharacteristicsBase, Plot, SoilSample
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
        fields = ['completed', 'plot', 'intensity', 'type', 'created_at']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_plot(self):
        plot = self.cleaned_data['plot']
        if SoilPreparation.objects.filter(plot=plot).exists():
            raise forms.ValidationError("Für diesen Schlag wurden bereits Bodenvorbereitungsdaten eingegeben.")
        return plot


class FertilizationForm(forms.ModelForm):
    class Meta:
        model = Fertilization
        fields = ['completed', 'plot', 'fertilizer', 'amount', 'created_at']
        # fields = ['field', 'plot', 'completed', 'fertilizer', 'amount', 'created_at']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # By default, either no plots or all plots can be displayed.
    #     # If you only want to show plots once a field is chosen, you might start with none:
    #     self.fields['plot'].queryset = Plot.objects.none()

    # # If a field was selected, filter the plots
    # if 'field' in self.data:
    #     try:
    #         field_id = self.data.get('field')
    #         if field_id:
    #             self.fields['plot'].queryset = Plot.objects.filter(field_id=field_id)
    #     except (ValueError, TypeError):
    #         # If the field_id is not valid, ignore and leave no plots.
    #         pass

    def clean_plot(self):
        plot = self.cleaned_data.get('plot')
        created_at = self.cleaned_data.get('created_at')  # Use `.get` to avoid KeyError
        print(plot)
        print(created_at)
        if plot and created_at:
            if Fertilization.objects.filter(plot=plot, created_at=created_at).exists():
                raise forms.ValidationError("Für diesen Schlag wurde bereits eine Düngung an diesem Datum eingetragen.")
        return plot


class SeedingForm(forms.ModelForm):
    class Meta:
        model = Seeding
        fields = ['plot', 'variety', 'seeding_rate', 'seedbed_width', 'thousand_grain_weight', 'created_at']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_plot(self):
        plot = self.cleaned_data['plot']
        if Seeding.objects.filter(plot=plot).exists():
            raise forms.ValidationError("Für diesen Schlag wurde bereits eine Aussaat eingetragen.")
        return plot


class TopCutForm(forms.ModelForm):
    class Meta:
        model = TopCut
        fields = ['plot', 'cutting_height', 'created_at']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_plot(self):
        plot = self.cleaned_data['plot']
        if TopCut.objects.filter(plot=plot).exists():
            raise forms.ValidationError("Für diesen Schlag wurde bereits ein Kopfschnitt eingetragen.")
        return plot


class WeedControlMechanicForm(forms.ModelForm):
    class Meta:
        model = WeedControlMechanic
        fields = ['plot', 'procedure', 'emergence']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        }


class WeedControlChemicalForm(forms.ModelForm):
    class Meta:
        model = WeedControlChemical
        fields = ['plot', 'substance', 'amount']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        }


class HarvestForm(forms.ModelForm):
    class Meta:
        model = Harvest
        fields = ['plot', 'procedure', 'created_at']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_plot(self):
        plot = self.cleaned_data['plot']
        if Harvest.objects.filter(plot=plot).exists():
            raise forms.ValidationError("Für diesen Schlag wurde bereits eine Ernte eingetragen.")
        return plot


class ConditioningForm(forms.ModelForm):
    class Meta:
        model = Conditioning
        fields = ['plot', 'procedure', 'created_at']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        }


class BailingForm(forms.ModelForm):
    class Meta:
        model = Bailing
        fields = ['plot', 'weight']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_plot(self):
        plot = self.cleaned_data['plot']
        if Bailing.objects.filter(plot=plot).exists():
            raise forms.ValidationError("Für diesen Schlag wurde bereits ein Ballen eingetragen.")
        return plot


class PlantCharacteristicsBaseForm(forms.ModelForm):
    class Meta:
        model = PlantCharacteristicsBase
        fields = ['plot', 'stem_thickness_one', 'stem_thickness_two', 'plant_density', 'topcut', 'shoots_number',
                  'growth_form']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        topcut = cleaned_data.get('topcut')
        shoots_number = cleaned_data.get('shoots_number')
        growth_form = cleaned_data.get('growth_form')

        if topcut:
            if not shoots_number:
                self.add_error('shoots_number', 'This field is required if "Topcut" is selected.')
            if not growth_form:
                self.add_error('growth_form', 'This field is required if "Topcut" is selected.')
        else:
            # Clear fields if topcut is not selected
            cleaned_data['shoots_number'] = None
            cleaned_data['growth_form'] = None

        return cleaned_data


class SoilSampleForm(forms.ModelForm):
    class Meta:
        model = SoilSample
        fields = ['plot', 'ph_value', 'cn_ratio', 'nitrogen_content', 'moisture_content', 'soil_texture',
                  'phosphorus_availability', 'salt_content', 'soil_compaction', 'sampling_date']

        widgets = {
            'sampling_date': forms.DateInput(attrs={'type': 'date'}),
        }
