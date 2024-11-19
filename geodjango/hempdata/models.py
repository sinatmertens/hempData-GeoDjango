from django.contrib.gis.db import models
from django.core.exceptions import ValidationError


class Field(models.Model):
    id = models.AutoField(primary_key=True)  # Automatic ID fiel Firled
    name = models.CharField(max_length=100)
    location = models.PolygonField()
    size = models.DecimalField(max_digits=10, decimal_places=2, editable=False,
                               verbose_name="Größe (ha)")  # Make size non-editable

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
    category = models.ForeignKey(SurveyCategory, on_delete=models.CASCADE, related_name='plots',
                                 verbose_name="Kategorie")
    location = models.PolygonField()  # Geometry of the plot for a specific category
    size = models.DecimalField(max_digits=10, decimal_places=2, editable=False,
                               verbose_name="Größe (ha)")  # Make size non-editable

    def save(self, *args, **kwargs):
        # Calculate area based on the polygon's geometry and convert to hectares
        if self.location:
            self.size = self.location.transform(3857, clone=True).area / 10000  # Area in hectares
        super().save(*args, **kwargs)

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
    seeding_rate = models.DecimalField(max_digits=5, decimal_places=2,
                                       verbose_name="Aussaatstärke (kg/ha)")  # Seeding rate in plants/m² or kg/ha
    fertilization_amount = models.DecimalField(max_digits=5, decimal_places=2,
                                               verbose_name="Düngemenge (kg N/ha)")  # Fertilizer amount in kg N/ha
    soil_preparation = models.CharField(max_length=100,
                                        verbose_name="Bodenvorbereitung (qual. Beschreibung)")  # Soil preparation method (qualitative)

    class Meta:
        verbose_name = "Feldvorbereitung"
        verbose_name_plural = "Feldvorbereitungen"

    def __str__(self):
        return f"Vorbereitungsdaten für Schlag {self.plot.id}"


class PlantCharacteristicsBase(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name='plant_characteristics_base', verbose_name="Schlag")
    # TODO: Notwendigkeit, Höhe auch händisch zu bestimmen?
    height = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Wuchshöhe")
    # TODO: Kategorisierung von Blattfarben?
    color = models.CharField(max_length=50, verbose_name="Blattfarbe")
    # TODO: Wie ist die Wuchsform anzugeben? Gerade, krumm? Oder Ranking?
    growth_form = models.CharField(max_length=50, verbose_name="Wuchsform")
    # TODO: Angabe in mm oder cm?
    stem_diameter = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Stängeldurchmesser")
    # TODO: Freies Textfeld?
    damage = models.TextField(verbose_name="Schaden (Wild, Hadel, etc.)")

    # TODO: Erhebungszeitraum

    class Meta:
        verbose_name = "Pflanzenmerkmal - unten"
        verbose_name_plural = "Pflanzenmerkmale - unten"

    def __str__(self):
        return f"Pflanzenmerkmale (unten) {self.id}"


class PlantCharacteristicsTop(models.Model):
    # TODO: Falls das die Tabelle für die Drohne ist, kommt hier sicherlich noch mehr
    id = models.AutoField(primary_key=True, verbose_name="ID")
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name='plant_characteristics_top', verbose_name="Schlag")

    # datetime

    class Meta:
        verbose_name = "Pflanzenmerkmale - oben"
        verbose_name_plural = "Pflanzenmerkmale - oben"

    def __str__(self):
        return f"Pflanzenmerkmale (oben) {self.id}"


class WeatherStation(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    location = models.PointField()

    # TODO: field # Auf welchem Feld steht die Wetterstation?
    # TODO: Exakte Position der Station
    # TODO: Modell name

    class Meta:
        verbose_name = "Wetterstation"
        verbose_name_plural = "Wetterstation"

    def __str__(self):
        return f"Wetterstation {self.id}"


class WeatherData(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")

    # TODO: ForeignKey zu welcher Wetterstation
    # TODO: Datetime der Datenaufnahme
    # TODO: Niederschlag
    # TODO: Wind
    # TODO: Sonnenstunden?
    # TODO: Luftfeuchtigkeit
    # TODO: Temperatur
    # TODO: Luftdruck
    # TODO: Bodentemperatur
    # TODO: Weitere Kennwerte?

    class Meta:
        verbose_name = "Wettermessung"
        verbose_name_plural = "Wettermessungen"

    def __str__(self):
        return f"Wettermessung {self.id}"


class SoilData(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name='soil_data', verbose_name="Schlag")

    # TODO: datetime
    # TODO: Bodenstrukturanalyse Tonanteil
    # TODO: soil_temperature
    # TODO: soil_moisture
    # TODO: soil_type
    # TODO: soil_texture
    # TODO: pH_value
    # TODO: Nmin (Nitrogen/Ammonium)
    # TODO: Plant Available Phosphorus
    # TODO: Soil Organic Matter
    # TODO: Soil Organic Carbon
    # TODO: Magnesium

    class Meta:
        verbose_name = "Bodenanalyse"
        verbose_name_plural = "Bodenanalysen"

    def __str__(self):
        return f"Bodenanalyse {self.id}"
