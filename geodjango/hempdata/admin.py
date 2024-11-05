from django import forms
from django.contrib.gis import admin
from .models import Field, SurveyCategory, Plot, PreparationData
from django.contrib.gis.geos import GEOSGeometry
from django.core.serializers import serialize

class PlotAdminForm(forms.ModelForm):
    location_input = forms.CharField(
        label="Polygon-Koordinaten (WKT oder GeoJSON)",
        widget=forms.Textarea,
        required=False
    )

    class Meta:
        model = Plot
        fields = ['field', 'category', 'location_input',]  # Removed 'size'

    def clean(self):
        cleaned_data = super().clean()
        location_input = cleaned_data.get("location_input")

        if location_input:
            try:
                geometry = GEOSGeometry(location_input)
                cleaned_data["location"] = geometry  # Set location from parsed geometry
            except Exception as e:
                raise forms.ValidationError(f"Invalid geometry format: {e}")
        elif not self.instance.location:
            raise forms.ValidationError("Please provide polygon coordinates as WKT or GeoJSON.")
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.cleaned_data.get("location_input"):
            instance.location = self.cleaned_data["location"]
        if commit:
            instance.save()
        return instance

# Admin for Plot with map display and additional input field
class PlotAdmin(admin.GISModelAdmin):
    form = PlotAdminForm
    default_lon = 12.2692
    default_lat = 51.2134
    default_zoom = 12
    srid = 4326
    list_display = ('id', 'field', 'category', 'size')
    list_filter = ('field', 'category')

    def changelist_view(self, request, extra_context=None):
        # Get all plots as GeoJSON
        plots_geojson = serialize('geojson', Plot.objects.all(), geometry_field='location')
        extra_context = extra_context or {}
        extra_context['plots_geojson'] = plots_geojson
        return super().changelist_view(request, extra_context=extra_context)

    class Media:
        css = {'all': ('https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/leaflet.css',)}
        js = ('https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/leaflet.js',)

# Admin for Field with map view
class FieldAdmin(admin.GISModelAdmin):
    default_lon = 12.2692
    default_lat = 51.2134
    default_zoom = 12
    srid = 4326
    list_display = ('name', 'size')

# Admin for SurveyCategory without map
class SurveyCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Admin for PreparationData
class PreparationDataAdmin(admin.ModelAdmin):
    list_display = ('plot','crop_type','seeding_rate','fertilization_amount','soil_preparation',)

# Register the models with their custom admin classes
admin.site.register(Field, FieldAdmin)
admin.site.register(SurveyCategory, SurveyCategoryAdmin)
admin.site.register(Plot, PlotAdmin)  # Only registered once now
admin.site.register(PreparationData, PreparationDataAdmin)
