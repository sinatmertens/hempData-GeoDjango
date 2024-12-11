from django import forms
from django.contrib.gis import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.gis.geos import GEOSGeometry
from django.core.exceptions import ValidationError
from .admin_resources import FieldResource
from .models import (
    Field, Plot, HistoricalData, SoilPreparation, Fertilization,
    Seeding, TopCut, WeedControlMechanic, WeedControlChemical,
    Harvest, Conditioning, Bailing, WeatherStation, WeatherData,
    PlantCharacteristicsTop, PlantCharacteristicsBase,
    SoilSample
)


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


class FieldAdmin(ImportExportModelAdmin):
    list_display = ('name', 'size',)
    form = FieldAdminForm
    resource_class = FieldResource  # Attach the resource class


# Form for Plot with GeoJSON or WKT input
class PlotAdminForm(LocationInputForm):
    class Meta:
        model = Plot
        fields = ['field', 'location_input']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.location = self.cleaned_data["location_input"]
        if commit:
            instance.save()
        return instance


# Admin for Plot with GeoJSON or WKT input
class PlotAdmin(ImportExportModelAdmin):
    form = PlotAdminForm
    list_display = ('name', 'field', 'size',)
    list_filter = ('field',)


class HistoricalDataInline(admin.TabularInline):
    model = HistoricalData
    extra = 0


class HistoricalDataAdmin(admin.ModelAdmin):
    list_display = ('plot', 'previous_crop1', 'previous_crop2', 'created_at')
    search_fields = ('plot__id',)


class SoilPreparationInline(admin.TabularInline):
    model = SoilPreparation
    extra = 0


class SoilPreparationAdmin(ImportExportModelAdmin):
    list_display = ('plot', 'intensity', 'type', 'completed', 'created_at')
    list_filter = ('intensity', 'completed')
    search_fields = ('plot__id',)


class PlantCharacteristicsBaseInline(admin.ModelAdmin):
    model = PlantCharacteristicsBase
    extra = 0


class PlantCharacteristicsBaseInlineAdmin(ImportExportModelAdmin):
    list_display = (
        'plot', 'stem_thickness_one', 'stem_thickness_two', 'plant_density', 'topcut', 'shoots_number', 'growth_form',
        'created_at')
    list_filter = ('plot', 'topcut')
    search_fields = ('plot__id',)


class FertilizationInline(admin.TabularInline):
    model = Fertilization
    extra = 0
    verbose_name = "Düngung"
    verbose_name_plural = "Düngungen"


class FertilizationAdmin(admin.ModelAdmin):
    list_display = ('plot', 'fertilizer', 'amount', 'completed', 'created_at')
    list_filter = ('fertilizer', 'completed')
    search_fields = ('plot__id',)


class SeedingInline(admin.TabularInline):
    model = Seeding
    extra = 0
    verbose_name = "Aussaat"
    verbose_name_plural = "Aussaaten"


class SeedingAdmin(admin.ModelAdmin):
    list_display = ('plot', 'variety', 'seeding_rate', 'thousand_grain_weight', 'created_at')
    search_fields = ('plot__id', 'variety')


class TopCutInline(admin.TabularInline):
    model = TopCut
    extra = 0
    verbose_name = "Schnitt"
    verbose_name_plural = "Schnitte"


class TopCutAdmin(admin.ModelAdmin):
    list_display = ('plot', 'cutting_height', 'created_at')
    search_fields = ('plot__id',)


class HarvestInline(admin.TabularInline):
    model = Harvest
    extra = 0
    verbose_name = "Ernte"
    verbose_name_plural = "Ernten"


class HarvestAdmin(admin.ModelAdmin):
    list_display = ('plot', 'procedure', 'created_at')
    list_filter = ('procedure',)
    search_fields = ('plot__id',)


class ConditioningInline(admin.TabularInline):
    model = Conditioning
    extra = 0
    verbose_name = "Konditionierung"
    verbose_name_plural = "Konditionierungen"


class ConditioningAdmin(admin.ModelAdmin):
    list_display = ('plot', 'procedure', 'created_at')
    list_filter = ('procedure',)
    search_fields = ('plot__id',)


class BailingInline(admin.TabularInline):
    model = Bailing
    extra = 0
    verbose_name = "Ballierung"
    verbose_name_plural = "Ballierungen"


class BailingAdmin(admin.ModelAdmin):
    list_display = ('plot', 'weight', 'created_at')
    search_fields = ('plot__id',)


class WeedControlMechanicInline(admin.TabularInline):
    model = WeedControlMechanic
    extra = 0


class WeedControlMechanicAdmin(ImportExportModelAdmin):
    list_display = ('plot', 'emergence', 'created_at')
    list_filter = ('emergence',)
    search_fields = ('plot__id',)


class WeedControlChemicalInline(admin.TabularInline):
    model = WeedControlChemical
    extra = 0


class WeedControlChemicalAdmin(admin.ModelAdmin):
    list_display = ('plot', 'substance', 'amount', 'created_at')
    search_fields = ('plot__id', 'substance')


class SoilSampleInline(admin.TabularInline):
    model = SoilSample
    extra = 0


class SoilSampleAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('plot', 'sampling_date', 'ph_value', 'cn_ratio', 'nitrogen_content', 'moisture_content',
                    'soil_texture', 'phosphorus_availability', 'salt_content', 'soil_compaction')
    search_fields = ('plot__name',)


# Register models with their custom admin classes
admin.site.register(Field, FieldAdmin)
admin.site.register(Plot, PlotAdmin)
admin.site.register(HistoricalData, HistoricalDataAdmin)
admin.site.register(SoilPreparation, SoilPreparationAdmin)
admin.site.register(Fertilization, FertilizationAdmin)
admin.site.register(Seeding, SeedingAdmin)
admin.site.register(TopCut, TopCutAdmin)
admin.site.register(WeedControlMechanic, WeedControlMechanicAdmin)
admin.site.register(WeedControlChemical, WeedControlChemicalAdmin)
admin.site.register(Harvest, HarvestAdmin)
admin.site.register(Conditioning, ConditioningAdmin)
admin.site.register(Bailing, BailingAdmin)
admin.site.register(PlantCharacteristicsBase, PlantCharacteristicsBaseInlineAdmin)
admin.site.register(SoilSample, SoilSampleAdmin)
