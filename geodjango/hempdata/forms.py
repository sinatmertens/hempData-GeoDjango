# yourapp/forms.py
from django import forms
from .models import HistoricalData

class HistoricalDataForm(forms.ModelForm):
    class Meta:
        model = HistoricalData
        fields = ['plot', 'previous_crop1', 'previous_crop2']
        labels = {
            'plot': 'Schlag',
            'previous_crop1': 'Vorfrucht 1',
            'previous_crop2': 'Vorfrucht 2',
        }
        widgets = {
            'plot': forms.Select(attrs={'class': 'form-control'}),
            'previous_crop1': forms.TextInput(attrs={'class': 'form-control'}),
            'previous_crop2': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_plot(self):
        plot = self.cleaned_data['plot']
        if HistoricalData.objects.filter(plot=plot).exists():
            raise forms.ValidationError("Für diesen Schlag wurden bereits historische Daten eingegeben.")
        return plot


