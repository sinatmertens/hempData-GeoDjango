# yourapp/forms.py
from django import forms
from .models import PreparationData

class PreparationDataForm(forms.ModelForm):
    class Meta:
        model = PreparationData
        fields = ['plot', 'crop_type', 'seeding_rate', 'fertilization_amount', 'soil_preparation']
        labels = {
            'plot': 'Wähle Schlag',
            'crop_type': 'Kulturart',
            'seeding_rate': 'Aussaatstärke (kg/ha)',
            'fertilization_amount': 'Düngemenge (kg N/ha)',
            'soil_preparation': 'Bodenvorbereitung (qual. Beschreibung)'
        }
