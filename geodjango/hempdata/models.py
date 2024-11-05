from django.contrib.gis.db import models
from django.core.exceptions import ValidationError


class Field(models.Model):
    id = models.AutoField(primary_key=True)  # Automatic ID fiel Firled
    name = models.CharField(max_length=100)
    location = models.PolygonField()
    size = models.DecimalField(max_digits=10, decimal_places=2, editable=False, verbose_name="Größe (ha)")  # Make size non-editable

    def save(self, *args, **kwargs):
        # Calculate area based on the polygon's geometry and convert to hectares (assuming SRID is 4326)
        if self.location:
            # Convert to an SRID suitable for area calculation if necessary
            self.size = self.location.transform(3857, clone=True).area / 10000  # Area in hectares
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Feld"  # Singular
        verbose_name_plural = "Felder"  # Plural

    def __str__(self):
        return self.name


# Category model for dividing into different survey types
class SurveyCategory(models.Model):
    id = models.AutoField(primary_key=True)  # Automatic ID for the category
    name = models.CharField(max_length=100)  # e.g., "Weather Measurement" or "Soil Quality"

    class Meta:
        verbose_name = "Kategorie"
        verbose_name_plural = "Kategorien"

    def __str__(self):
        return self.name


# Plot model for individual divisions of a field
class Plot(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Schlag ID")  # Automatic ID for the plot
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='plots', verbose_name="In Feld")
    category = models.ForeignKey(SurveyCategory, on_delete=models.CASCADE, related_name='plots', verbose_name="Kategorie")
    location = models.PolygonField()  # Geometry of the plot for a specific category
    size = models.DecimalField(max_digits=10, decimal_places=2, editable=False, verbose_name="Größe (ha)")  # Make size non-editable
    def save(self, *args, **kwargs):
        # Calculate area based on the polygon's geometry and convert to hectares
        if self.location:
            self.size = self.location.transform(3857, clone=True).area / 10000  # Area in hectares
        super().save(*args, **kwargs)

    #def clean(self):
    #    # Constraint 1: Ensure the plot is fully within the field
    #    if not self.field.location.contains(self.location):
    #        raise ValidationError("The plot must be fully contained within the field.")

    #    # Constraint 2: Ensure plots of the same category do not overlap within the same field
    #    overlapping_plots = Plot.objects.filter(field=self.field, category=self.category).exclude(id=self.id)
    #    for other_plot in overlapping_plots:
    #        if self.location.intersects(other_plot.location):
    #            raise ValidationError("Plots within the same category must not overlap.")

    #    super().clean()

    class Meta:
        verbose_name = "Schlag"
        verbose_name_plural = "Schläge"

    def __str__(self):
        return f"Schlag {self.id} in {self.field.name}"


# Preparation Data model for field setup information
class PreparationData(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name='preparation_data', verbose_name="Schlag")
    crop_type = models.CharField(max_length=100, verbose_name="Kulturart")  # Crop type (e.g., hemp variety)
    seeding_rate = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Aussaatstärke (kg/ha)")  # Seeding rate in plants/m² or kg/ha
    fertilization_amount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Düngemenge (kg N/ha)")  # Fertilizer amount in kg N/ha
    soil_preparation = models.CharField(max_length=100, verbose_name="Bodenvorbereitung (qual. Beschreibung)")  # Soil preparation method (qualitative)

    class Meta:
        verbose_name = "Feldvorbereitung"
        verbose_name_plural = "Feldvorbereitungen"

    def __str__(self):
        return f"Vorbereitungsdaten für Schlag {self.plot.id}"