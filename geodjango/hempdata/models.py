from django.contrib.gis.db import models
from django.utils.timezone import now
import uuid

class Field(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    name = models.CharField(max_length=255, verbose_name="Name des Feldes",
                            help_text="Der Name des Feldes, um es eindeutig zu identifizieren.")
    size = models.IntegerField(verbose_name="Größe des Feldes (m²)", help_text="Die Größe des Feldes in Quadratmetern.")
    location = models.PolygonField(verbose_name="Geographische Lage",
                                   help_text="Polygongeometrie zur Darstellung der geographischen Lage des Feldes.")
    created_at = models.DateField(auto_now_add=True, verbose_name="Erhebungszeitpunkt")

    class Meta:
        verbose_name = "Standort - Feld"
        verbose_name_plural = "Standort - Felder"

    def __str__(self):
        return self.name


class Plot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name="plots", verbose_name="Zugehöriges Feld",
                              help_text="Das Feld, dem dieser Schlag zugeordnet ist.")
    name = models.CharField(max_length=255, verbose_name="Name des Schlags",
                            help_text="Der Name des Schlags, um ihn eindeutig zu identifizieren.")
    size = models.IntegerField(verbose_name="Größe des Schlags (m²)",
                               help_text="Die Größe des Schlags in Quadratmetern.")
    location = models.PolygonField(verbose_name="Geographische Lage",
                                   help_text="Polygongeometrie zur Darstellung der geographischen Lage des Schlags.")
    created_at = models.DateField(auto_now_add=True, verbose_name="Erhebungszeitpunkt",
                                  help_text="Datum, an dem der Schlag erfasst wurde.")

    class Meta:
        verbose_name = "Standort - Schlag"
        verbose_name_plural = "Standort - Schläge"

    def __str__(self):
        return f"{self.name}"


class WeatherStation(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    location = models.PointField(verbose_name="Standort",
                                 help_text="Geographische Punktposition der Wetterstation, um den genauen Standort anzugeben.")

    class Meta:
        verbose_name = "Standort - Wetterstation"
        verbose_name_plural = "Standort - Wetterstationen"

    def __str__(self):
        return f"Wetterstation {self.id}"




class HistoricalData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID",
                          help_text="Eindeutige ID der historischen Daten.")
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="historical_data", verbose_name="Schlag *",
                             help_text="Das Feld (Plot), dem diese historischen Daten zugeordnet sind.")
    previous_crop1 = models.CharField(max_length=255, verbose_name="Vorfrucht 1",
                                      help_text="Die erste Vorfrucht, die im Vorjahr auf diesem Schlag angebaut wurde.")
    previous_crop2 = models.CharField(max_length=255, verbose_name="Vorfrucht 2",
                                      help_text="Die zweite Vorfrucht, die vor zwei Jahren auf diesem Schlag angebaut wurde.")
    created_at = models.DateField(auto_now_add=True, verbose_name="Erhebungszeitpunkt",
                                  help_text="Das Datum, an dem die historischen Daten erfasst wurden.")

    class Meta:
        verbose_name = "Historische Daten"
        verbose_name_plural = "Historische Daten"
        constraints = [
            models.UniqueConstraint(fields=['plot'], name='unique_plot_historical_data')
        ]

    def __str__(self):
        return f"Historische Daten für {self.plot.name}"


class SoilPreparation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID",
                          help_text="Eindeutige ID der Bodenvorbereitung.")

    INTENSITY_CHOICES = [
        ('flach', 'Flach'),
        ('mittel', 'Mittel'),
        ('tief', 'Tief'),
    ]

    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="soil_preparation", verbose_name="Schlag *",
                             help_text="Der Schlag, für den die Bodenvorbereitung durchgeführt wurde.")
    completed = models.BooleanField(default=True, verbose_name="Durchgeführt")
    intensity = models.CharField(max_length=10, choices=INTENSITY_CHOICES, verbose_name="Intensität",
                                 help_text="Die Intensität der Bodenvorbereitung (Flach, Mittel, Tief).")
    type = models.CharField(max_length=255, verbose_name="Art der Durchführung",
                            help_text="Die Art der durchgeführten Bodenvorbereitung (z. B. Pflügen, Eggen).")
    created_at = models.DateField(default=now, verbose_name="Datum *",
                                  help_text="Das Datum, an dem die Düngung durchgeführt wurde.")

    class Meta:
        verbose_name = "Prozessdaten 1 - Bodenvorbereitung"
        verbose_name_plural = "Prozessdaten 1 - Bodenvorbereitungen"

    def __str__(self):
        return f"Bodenvorbereitung für {self.plot.name}"


class Fertilization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID",
                          help_text="Eindeutige ID der Düngung.")

    FERTILIZER_CHOICES = [
        ('type1', 'Type 1'),  # Example placeholders for fertilizer types
        ('type2', 'Type 2'),
        ('type3', 'Type 3'),
    ]

    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="fertilizations", verbose_name="Schlag *",
                             help_text="Der Schlag, für den die Düngung durchgeführt wurde.")
    completed = models.BooleanField(default=True, verbose_name="Düngung erfolgt",
                                    help_text="Gibt an, ob die Düngung abgeschlossen wurde.")
    fertilizer = models.CharField(max_length=50, choices=FERTILIZER_CHOICES, verbose_name="Dünger",
                                  help_text="Der verwendete Dünger (z. B. NPK, Kalk).")
    amount = models.IntegerField(verbose_name="Menge (kg/ha)", help_text="Die Düngermenge pro Hektar (kg/ha).")
    created_at = models.DateField(default=now, verbose_name="Datum *",
                                  help_text="Das Datum, an dem die Düngung durchgeführt wurde.")

    class Meta:
        verbose_name = "Prozessdaten 2 - Düngung"
        verbose_name_plural = "Prozessdaten 2 - Düngung"

    def __str__(self):
        return f"Düngung für {self.plot.name} am {self.created_at}"


class Seeding(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID",
                          help_text="Eindeutige ID der Aussaat.")
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="seedings", verbose_name="Schlag *",
                             help_text="Der Schlag, für den die Aussaat durchgeführt wurde.")
    variety = models.CharField(max_length=255, verbose_name="Kulturart",
                               help_text="Die Kulturart (z.B. Weizen, Mais), die ausgesät wurde.")
    seeding_rate = models.IntegerField(verbose_name="Ausaatstärke (kg/ha)",
                                       help_text="Die Menge an Saatgut, die pro Hektar ausgesät wurde (in kg/ha).")
    seedbed_width = models.IntegerField(verbose_name="Saatbettreite (cm)",
                                        help_text="Die Breite des Saatbettes in Zentimetern.")
    thousand_grain_weight = models.FloatField(default=12.5, verbose_name="Tausendkorngewicht (g)",
                                              help_text="Das Gewicht von tausend Körnern der ausgesäten Kultur (in Gramm).")
    created_at = models.DateField(default=now, verbose_name="Datum *",
                                  help_text="Das Datum, an dem die Aussaat vorgenommen wurde.")

    class Meta:
        verbose_name = "Prozessdaten 3 - Aussaat"
        verbose_name_plural = "Prozessdaten 3 - Aussaat"

    def __str__(self):
        return f"Aussaat für {self.plot.name} - {self.variety}"


class TopCut(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID",
                          help_text="Eindeutige ID des Kopfschnitts.")
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="topcuts", verbose_name="Schlag *",
                             help_text="Der Schlag, für den der Kopfschnitt durchgeführt wurde.")
    cutting_height = models.IntegerField(verbose_name="Schnitthöhe",
                                         help_text="Die Höhe, auf der der Kopfschnitt durchgeführt wurde (in cm).")
    created_at = models.DateField(default=now, verbose_name="Datum *",
                                  help_text="Das Datum, an dem der Topcut stattgefunden hat.")

    class Meta:
        verbose_name = "Bestandspflege - Kopfschnitt"
        verbose_name_plural = "Bestandspflege - Kopfschnitt"

    def __str__(self):
        return f"Kopfschnitt für {self.plot.name}"


class WeedControlMechanic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID",
                          help_text="Eindeutige ID der mechanischen Unkrautbekämpfung.")

    EMERGENCE_CHOICES = [
        ('Nach dem Auflauf', 'Nach dem Auflauf'),
        ('Vor dem Auflauf', 'Vor dem Auflauf'),
    ]

    CONTROL_CHOICES = [
        ('Hacken', 'Hacken'),
        ('Striegeln', 'Striegeln'),
        ('Rollen', 'Rollen'),
    ]

    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="mechanic_weed_controls",
                             verbose_name="Schlag *",
                             help_text="Der Schlag, für den die mechanische Unkrautbekämpfung durchgeführt wurde.")
    procedure = models.CharField(max_length=20, choices=CONTROL_CHOICES, verbose_name="Prozess",
                                 help_text="Gibt an, welche Art von Unkrautbekämpfung durchgeführt wurde.")
    emergence = models.CharField(max_length=20, choices=EMERGENCE_CHOICES, verbose_name="Nach/Vor dem Auflauf",
                                 help_text="Gibt an, ob die Unkrautbekämpfung vor oder nach dem Auflaufen der Kultur durchgeführt wurde.")
    created_at = models.DateField(default=now, verbose_name="Datum *",
                                  help_text="Das Datum, an dem die Unkrautbekämpfung vorgenommen wurde.")

    class Meta:
        verbose_name = "Bestandspflege - Unkrautbekämpfung - Mechanisch"
        verbose_name_plural = "Bestandspflege - Unkrautbekämpfung - Mechanisch"

    def __str__(self):
        return f"Mechanische Unkrautbekämpfung für {self.plot.name}"


class WeedControlChemical(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID",
                          help_text="Eindeutige ID der chemischen Unkrautbekämpfung.")
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="chemical_weed_controls",
                             verbose_name="Schlag *",
                             help_text="Der Schlag, auf dem die chemische Unkrautbekämpfung durchgeführt wurde.")
    substance = models.CharField(max_length=255, verbose_name="Substanz",
                                 help_text="Die verwendete chemische Substanz zur Unkrautbekämpfung.")
    amount = models.IntegerField(verbose_name="Menge",
                                 help_text="Die ausgebrachte Menge der chemischen Substanz.")
    created_at = models.DateField(default=now, verbose_name="Erhebungszeitpunkt",
                                  help_text="Das Datum, an dem die Anwendung der chemischen Unkrautbekämpfung erfasst wurde.")

    class Meta:
        verbose_name = "Bestandspflege - Unkrautbekämpfung - Chemisch"
        verbose_name_plural = "Bestandspflege - Unkrautbekämpfung - Chemisch"


class Harvest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID",
                          help_text="Eindeutige ID der Ernteerfassung.")
    PROCEDURE_CHOICES = [
        ('Wirr', 'Wirr'),
        ('Parallel', 'Parallel'),
    ]
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="harvests", verbose_name="Schlag *",
                             help_text="Der Schlag, für den die Ernte vorgenommen wurde.")
    procedure = models.CharField(max_length=20, choices=PROCEDURE_CHOICES, verbose_name="Ernte-Prozedur",
                                 help_text="Verfahren, nach dem die Ernte durchgeführt wurde.")
    created_at = models.DateField(default=now, verbose_name="Datum *",
                                  help_text="Das Datum, an dem die Ernte durchgeführt wurde.")

    class Meta:
        verbose_name = "Prozessdaten 7 - Ernte"
        verbose_name_plural = "Prozessdaten 7 - Ernte"



class Conditioning(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID",
                          help_text="Eindeutige ID der Konditionierungserfassung.")
    PROCEDURE_CHOICES = [
        ('Wenden', 'Wenden'),
        ('Lüften', 'Lüften'),
    ]
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="conditioning", verbose_name="Schlag *",
                             help_text="Der Schlag, in dem die Konditionierungsmaßnahmen durchgeführt wurden.")
    procedure = models.CharField(max_length=20, choices=PROCEDURE_CHOICES, verbose_name="Prozedur",
                                 help_text="Die angewandte Prozedur zur Nachbehandlung des Ernteguts.")
    created_at = models.DateField(default=now, verbose_name="Datum *",
                                  help_text="Das Datum, an dem die Konditionierung durchgeführt wurde.")

    class Meta:
        verbose_name = "Prozessdaten 8 - Konditionierung"
        verbose_name_plural = "Prozessdaten 8 - Konditionierung"


class Bailing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="bailings", verbose_name="Schlag *")
    weight = models.IntegerField(verbose_name="Gewicht")
    created_at = models.DateField(auto_now_add=True, verbose_name="Erhebungszeitpunkt")

    class Meta:
        verbose_name = "Prozessdaten 9 - Ballen"  # Singular
        verbose_name_plural = "Prozessdaten 9 - Ballen"  # Plural


class PlantCharacteristicsBase(models.Model):
    PERCENT_CHOICES = [(10, '10%'),
                       (20, '20%'),
                       (30, '30%'),
                       (40, '40%'),
                       (50, '50%'),
                       (60, '60%'),
                       (70, '70%'),
                       (80, '80%'),
                       (90, '90%'),
                       (100, '100%')]

    id = models.AutoField(primary_key=True, verbose_name="ID")
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name='plant_characteristics_base',
                             verbose_name="Schlag *")
    stem_thickness_one = models.IntegerField(verbose_name="Stängeldicke - Messstelle 1 - (x cm von Boden)")
    stem_thickness_two = models.IntegerField(verbose_name="Stängeldicke - Messstelle 2 - (x cm von Boden)")
    plant_density = models.IntegerField(verbose_name="Pflanzendichte (Pflanzen pro qm)")
    topcut = models.BooleanField(verbose_name="Topcut")
    shoots_number = models.IntegerField(choices=PERCENT_CHOICES,
                                        verbose_name="Topcut-Triebzahl (%-Anteil Doppeltriebe)", null=True, blank=True)
    growth_form = models.IntegerField(choices=PERCENT_CHOICES, verbose_name="Wuchsform (%-Anteil gerade)", null=True,
                                      blank=True)

    # Raster
    created_at = models.DateField(auto_now_add=True, verbose_name="Erhebungszeitpunkt")

    class Meta:
        verbose_name = "Verlaufsanalytik - Manuell- Pflanzenmerkmale"
        verbose_name_plural = "Verlaufsanalytik - Manuell- Pflanzenmerkmale"

    def __str__(self):
        return f"Pflanzenmerkmale (unten) {self.id}"


class PlantCharacteristicsTop(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name='plant_characteristics_top',
                             verbose_name="Schlag *")
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


class SoilSample(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")

    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name='soil_samples', verbose_name="Schlag *")

    # Typische Messwerte für Bodenproben (allowed to be empty)
    ph_value = models.FloatField(verbose_name="pH-Wert", help_text="pH-Wert des Bodens", null=True, blank=True)
    cn_ratio = models.FloatField(verbose_name="C/N Verhältnis", help_text="Verhältnis von Kohlenstoff zu Stickstoff",
                                 null=True, blank=True)
    nitrogen_content = models.FloatField(verbose_name="Stickstoffgehalt (g/kg)",
                                         help_text="Stickstoffgehalt des Bodens in g/kg", null=True, blank=True)
    moisture_content = models.FloatField(verbose_name="Bodenfeuchtigkeit (%)", help_text="Feuchtigkeit des Bodens in %",
                                         null=True, blank=True)
    soil_texture = models.CharField(max_length=100, verbose_name="Bodenart",
                                    help_text="Bodenart (z.B. sandig, lehmig, tonig)", null=True, blank=True)
    phosphorus_availability = models.FloatField(verbose_name="Phosphorverfügbarkeit (mg/kg)",
                                                help_text="Verfügbarkeit von Phosphor im Boden", null=True, blank=True)
    salt_content = models.FloatField(verbose_name="Salzgehalt (g/kg)", help_text="Salzgehalt des Bodens in g/kg",
                                     null=True, blank=True)
    soil_compaction = models.FloatField(verbose_name="Bodenverdichtung (kg/cm²)",
                                        help_text="Bodenverdichtung in kg/cm²", null=True, blank=True)

    # Zeitpunkt der Probenahme (not allowed to be empty)
    sampling_date = models.DateField(verbose_name="Probenahmedatum *", help_text="Datum der Bodenprobenahme")

    class Meta:
        verbose_name = "Verlaufsanalytik - Manuell- Bodenproben"
        verbose_name_plural = "Verlaufsanalytik - Manuell- Bodenproben"

    def __str__(self):
        return f"Bodenprobe {self.id} - {self.plot.name}"
