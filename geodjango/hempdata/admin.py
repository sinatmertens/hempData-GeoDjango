from django import forms
from django.contrib.gis import admin
from .models import Field, SurveyCategory, Plot, PreparationData
from django.contrib.gis.geos import GEOSGeometry
from django.core.serializers import serialize
from django.core.exceptions import ValidationError

# Shared form functionality for handling GeoJSON or WKT inputs
class LocationInputForm(forms.ModelForm):
    location_input = forms.CharField(
        label="Polygon-Koordinaten (WKT oder GeoJSON)",
        widget=forms.Textarea,
        required=False
    )

    def clean_location_input(self):
        location_input = self.cleaned_data.get("location_input")
        if location_input:
            try:
                return GEOSGeometry(location_input)
            except Exception as e:
                raise ValidationError(f"Invalid geometry format: {e}")
        raise ValidationError("Please provide polygon coordinates in WKT or GeoJSON.")

# Form for Plot with GeoJSON or WKT input
class PlotAdminForm(LocationInputForm):
    class Meta:
        model = Plot
        fields = ['field', 'category', 'location_input']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.location = self.cleaned_data["location_input"]
        if commit:
            instance.save()
        return instance

# Form for Field with GeoJSON or WKT input
class FieldAdminForm(LocationInputForm):
    class Meta:
        model = Field
        fields = ['name', 'location_input']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.location = self.cleaned_data["location_input"]
        if commit:
            instance.save()
        return instance

# Admin for Plot with GeoJSON or WKT input
class PlotAdmin(admin.ModelAdmin):
    form = PlotAdminForm
    list_display = ('id', 'field', 'category', 'size')
    list_filter = ('field', 'category')

# Admin for Field with GeoJSON or WKT input
class FieldAdmin(admin.ModelAdmin):
    form = FieldAdminForm
    list_display = ('name', 'size')

# Admin for SurveyCategory without map
class SurveyCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Admin for PreparationData
class PreparationDataAdmin(admin.ModelAdmin):
    list_display = ('plot', 'crop_type', 'seeding_rate', 'fertilization_amount', 'soil_preparation')

# Register models with their custom admin classes
admin.site.register(Field, FieldAdmin)
admin.site.register(SurveyCategory, SurveyCategoryAdmin)
admin.site.register(Plot, PlotAdmin)
admin.site.register(PreparationData, PreparationDataAdmin)
