from django import forms
from .models import (
    HistoricalData,
    SoilPreparation, Fertilization,
    Seeding, TopCut, WeedControlMechanic, WeedControlChemical,
    Harvest, Conditioning, Bailing, WeatherStation, WeatherData,
    PlantCharacteristicsTop, PlantCharacteristicsBase, Plot, SoilSample
)


#
class HistoricalDataForm(forms.ModelForm):
    class Meta:
        model = HistoricalData
        fields = ['plot', 'previous_crops', 'sommerung', 'winterung']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        }


class SoilPreparationForm(forms.ModelForm):
    class Meta:
        model = SoilPreparation
        fields = ['plot', 'intensity', 'type', 'additional_information', 'created_at']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        }


class FertilizationForm(forms.ModelForm):
    class Meta:
        model = Fertilization
        fields = ['plot', 'fertilizer', 'dosage_form', 'amount', 'created_at']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        }


class SeedingForm(forms.ModelForm):
    class Meta:
        model = Seeding
        fields = ['plot', 'variety', 'sorte', 'seeding_rate', 'seedbed_width', 'thousand_grain_weight', 'created_at']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        }


class TopCutForm(forms.ModelForm):
    class Meta:
        model = TopCut
        fields = ['plot', 'cutting_height', 'created_at']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        }


class WeedControlMechanicForm(forms.ModelForm):
    class Meta:
        model = WeedControlMechanic
        fields = ['plot', 'procedure', 'procedure_text', 'emergence', 'created_at']
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
        fields = ['plotpart', 'procedure', 'created_at']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        }


class ConditioningForm(forms.ModelForm):
    class Meta:
        model = Conditioning
        fields = ['plotpart', 'procedure', 'created_at']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        }


class BailingForm(forms.ModelForm):
    class Meta:
        model = Bailing
        fields = ['plotpart', 'procedure', 'weight', 'amount']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        }


class PlantCharacteristicsBaseForm(forms.ModelForm):
    class Meta:
        model = PlantCharacteristicsBase
        fields = ['plot', 'stem_thickness', 'plant_density', 'topcut', 'shoots_number',
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
                  'phosphorus_availability', 'salt_content', 'sampling_date']

        widgets = {
            'sampling_date': forms.DateInput(attrs={'type': 'date'}),
        }
