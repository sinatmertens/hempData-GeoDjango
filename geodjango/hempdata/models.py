from django.contrib.gis.db import models
from django.utils.timezone import now
from datetime import date
import uuid


class Field(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    name = models.CharField(max_length=255)
    size = models.IntegerField()
    location = models.PolygonField()
    created_at = models.DateField(auto_now_add=True, verbose_name="Erhebungszeitpunkt")

    class Meta:
        verbose_name = "Standort - Feld"  # Singular
        verbose_name_plural = "Standort - Felder"  # Plural

    def __str__(self):
        return self.name


class Plot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name="plots")
    name = models.CharField(max_length=255)
    size = models.IntegerField()
    location = models.PolygonField()
    created_at = models.DateField(auto_now_add=True, verbose_name="Erhebungszeitpunkt")

    class Meta:
        verbose_name = "Standort - Schlag"  # Singular
        verbose_name_plural = "Standort - Schläge"  # Plural

    def __str__(self):
        return f"{self.field.name} - {self.name}"


class WeatherStation(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    location = models.PointField(verbose_name="Standort")

    class Meta:
        verbose_name = "Standort - Wetterstation"
        verbose_name_plural = "Standort - Wetterstationen"

    def __str__(self):
        return f"Wetterstation {self.id}"


class HistoricalData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="historical_data", verbose_name="Schlag")
    previous_crop1 = models.CharField(max_length=255, verbose_name="Vorfrucht 1")
    previous_crop2 = models.CharField(max_length=255, verbose_name="Vorfrucht 2")
    created_at = models.DateField(auto_now_add=True, verbose_name="Erhebungszeitpunkt")

    class Meta:
        verbose_name = "Historische Daten"
        verbose_name_plural = "Historische Daten"
        constraints = [
            models.UniqueConstraint(fields=['plot'], name='unique_plot_historical_data')
        ]


class SoilPreparation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    INTENSITY_CHOICES = [
        ('flach', 'Flach'),
        ('mittel', 'Mittel'),
        ('tief', 'Tief'),
    ]
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="soil_preparations", verbose_name="Schlag")
    completed = models.BooleanField(default=True, verbose_name="Durchgeführt")
    intensity = models.CharField(max_length=10, choices=INTENSITY_CHOICES, verbose_name="Intensität")
    type = models.CharField(max_length=255, verbose_name="Art der Durchführung")
    created_at = models.DateField(auto_now_add=True, verbose_name="Erhebungszeitpunkt")

    class Meta:
        verbose_name = "Prozessdaten 1 - Bodenvorbereitung"  # Singular
        verbose_name_plural = "Prozessdaten 1 - Bodenvorbereitungen"  # Plural


class Fertilization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    FERTILIZER_CHOICES = [
        ('type1', 'Type 1'),  # Replace '?' with actual options
        ('type2', 'Type 2'),
        ('type3', 'Type 3'),
    ]
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="fertilizations", verbose_name="Schlag")
    completed = models.BooleanField(default=True, verbose_name="Düngung erfolgt")
    fertilizer = models.CharField(max_length=50, choices=FERTILIZER_CHOICES, verbose_name="Dünger")
    amount = models.IntegerField(verbose_name="Menge (kg/ha)")  # kg/ha
    created_at = models.DateField(default=now, verbose_name="Zeitpunkt der Düngung")

    class Meta:
        verbose_name = "Prozessdaten 2 - Düngung"  # Singular
        verbose_name_plural = "Prozessdaten 2 - Düngung"  # Plural


class Seeding(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="seedings", verbose_name="Schlag")
    variety = models.CharField(max_length=255, verbose_name="Kulturart")
    seeding_rate = models.IntegerField(verbose_name="Ausaatstärke (kg/ha)")
    seedbed_width = models.IntegerField(verbose_name="Tausendkorngewicht (kg)")
    thousand_grain_weight = models.FloatField(default=12.5, verbose_name="•	Saatbettreite (cm)")
    created_at = models.DateField(auto_now_add=True, verbose_name="Erhebungszeitpunkt")

    class Meta:
        verbose_name = "Prozessdaten 3 - Aussaat"  # Singular
        verbose_name_plural = "Prozessdaten 3 - Aussaat"  # Plural


class TopCut(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="topcuts", verbose_name="Schlag")
    cutting_height = models.IntegerField(verbose_name="Schnitthöhe")
    created_at = models.DateField(auto_now_add=True, verbose_name="Erhebungszeitpunkt")

    class Meta:
        verbose_name = "Bestandspflege - Kopfschnitt"  # Singular
        verbose_name_plural = "Bestandspflege - Kopfschnitt"  # Singular


class WeedControlMechanic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    EMERGENCE_CHOICES = [
        ('Nach dem Auflauf', 'Nach dem Auflauf'),
        ('Vor dem Auflauf', 'Vor dem Auflauf'),
    ]
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="mechanic_weed_controls", verbose_name="Schlag")
    hacken = models.BooleanField(default=False, verbose_name="Hacken")
    striegeln = models.BooleanField(default=False, verbose_name="Striegeln")
    rollen = models.BooleanField(default=False, verbose_name="Rollen")
    emergence = models.CharField(max_length=20, choices=EMERGENCE_CHOICES, verbose_name="Nach/Vor dem Auflauf")
    created_at = models.DateField(auto_now_add=True, verbose_name="Erhebungszeitpunkt")

    class Meta:
        verbose_name = "Bestandspflege - Unkrautbekämpfung - Mechanisch"  # Singular
        verbose_name_plural = "Bestandspflege - Unkrautbekämpfung - Mechanisch"  # Singular


class WeedControlChemical(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="chemical_weed_controls", verbose_name="Schlag")
    substance = models.CharField(max_length=255, verbose_name="Substanz")
    amount = models.IntegerField(verbose_name="Menge")
    created_at = models.DateField(auto_now_add=True, verbose_name="Erhebungszeitpunkt")

    class Meta:
        verbose_name = "Bestandspflege - Unkrautbekämpfung - Chemisch"  # Singular
        verbose_name_plural = "Bestandspflege - Unkrautbekämpfung - Chemisch"  # Plural


class Harvest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    PROCEDURE_CHOICES = [
        ('Wirr', 'Wirr'),
        ('Parallel', 'Parallel'),
    ]
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="harvests", verbose_name="Schlag")
    procedure = models.CharField(max_length=20, choices=PROCEDURE_CHOICES, verbose_name="Prozedur")
    created_at = models.DateField(auto_now_add=True, verbose_name="Erhebungszeitpunkt")

    class Meta:
        verbose_name = "Prozessdaten 7 - Ernte"  # Singular
        verbose_name_plural = "Prozessdaten 7 - Ernte"  # Plural


class Conditioning(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    PROCEDURE_CHOICES = [
        ('Wenden', 'Wenden'),
        ('Lüften', 'Lüften'),
    ]
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="conditioning", verbose_name="Schlag")
    procedure = models.CharField(max_length=20, choices=PROCEDURE_CHOICES, verbose_name="Prozedur")
    created_at = models.DateField(auto_now_add=True, verbose_name="Erhebungszeitpunkt")

    class Meta:
        verbose_name = "Prozessdaten 8 - Konditionierung"  # Singular
        verbose_name_plural = "Prozessdaten 8 - Konditionierung"  # Plural


class Bailing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="bailings", verbose_name="Schlag")
    weight = models.IntegerField(verbose_name="Gewicht")
    created_at = models.DateField(auto_now_add=True, verbose_name="Erhebungszeitpunkt")

    class Meta:
        verbose_name = "Prozessdaten 9 - Ballen"  # Singular
        verbose_name_plural = "Prozessdaten 9 - Ballen"  # Plural


class PlantCharacteristicsBase(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name='plant_characteristics_base',
                             verbose_name="Schlag")
    # Raster
    created_at = models.DateField(auto_now_add=True, verbose_name="Erhebungszeitpunkt")

    class Meta:
        verbose_name = "Verlaufsanalytik - Pflanzenmerkmal - Analog"
        verbose_name_plural = "Verlaufsanalytik - Pflanzenmerkmale - Analog"

    def __str__(self):
        return f"Pflanzenmerkmale (unten) {self.id}"


class PlantCharacteristicsTop(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name='plant_characteristics_top',
                             verbose_name="Schlag")
    created_at = models.DateField(auto_now_add=True, verbose_name="Erhebungszeitpunkt")

    class Meta:
        verbose_name = "Verlaufsanalytik - Pflanzenmerkmale - Drohne"
        verbose_name_plural = "Verlaufsanalytik - Pflanzenmerkmale - Drohne"

    def __str__(self):
        return f"Pflanzenmerkmale (oben) {self.id}"


class WeatherData(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")

    class Meta:
        verbose_name = "Verlaufsanalytik - Wettermessung"
        verbose_name_plural = "Verlaufsanalytik - Wettermessungen"

    def __str__(self):
        return f"Wettermessung {self.id}"


class SoilData(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name='soil_data', verbose_name="Schlag")

    class Meta:
        verbose_name = "Verlaufsanalytik - Bodenanalyse"
        verbose_name_plural = "Verlaufsanalytik - Bodenanalysen"

    def __str__(self):
        return f"Bodenanalyse {self.id}"
