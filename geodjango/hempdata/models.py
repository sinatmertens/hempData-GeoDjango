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


class PlotParts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="plots", verbose_name="Zugehöriger Schlag",
                              help_text="Der Schlag, dem dieser Teilschlags zugeordnet ist.")
    name = models.CharField(max_length=255, verbose_name="Name des Teilschlags",
                            help_text="Der Name des Teilschlags, um ihn eindeutig zu identifizieren.")
    size = models.IntegerField(verbose_name="Größe des Teilschlags (m²)",
                               help_text="Die Größe des Teilschlags in Quadratmetern.")
    location = models.PolygonField(verbose_name="Geographische Lage",
                                   help_text="Polygongeometrie zur Darstellung der geographischen Lage des Teilschlags.")
    created_at = models.DateField(auto_now_add=True, verbose_name="Erhebungszeitpunkt",
                                  help_text="Datum, an dem der Teilschlags erfasst wurde.")

    class Meta:
        verbose_name = "Standort - Teilschlag"
        verbose_name_plural = "Standort - Teilschläge"

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
    WINTERUNG_CHOICES = [
        ("2024/2025 Winterung", "2024/2025 Winterung"),
        ("2023/2024 Winterung", "2023/2024 Winterung"),
        ("2022/2023 Winterung", "2022/2023 Winterung"),
        ("2021/2022 Winterung", "2021/2022 Winterung"),
        ("2020/2021 Winterung", "2020/2021 Winterung"),
        ("2019/2020 Winterung", "2019/2020 Winterung"),
        ("2018/2019 Winterung", "2018/2019 Winterung"),
        ("2017/2018 Winterung", "2017/2018 Winterung"),
        ("2016/2017 Winterung", "2016/2017 Winterung"),
        ("2015/2016 Winterung", "2015/2016 Winterung"),
        ("2014/2015 Winterung", "2014/2015 Winterung"),
        ("2013/2014 Winterung", "2013/2014 Winterung"),
        ("2012/2013 Winterung", "2012/2013 Winterung"),
        ("2011/2012 Winterung", "2011/2012 Winterung"),
        ("2010/2011 Winterung", "2010/2011 Winterung"),
        ("2009/2010 Winterung", "2009/2010 Winterung"),
        ("2008/2009 Winterung", "2008/2009 Winterung"),
        ("2007/2008 Winterung", "2007/2008 Winterung"),
        ("2006/2007 Winterung", "2006/2007 Winterung"),
        ("2005/2006 Winterung", "2005/2006 Winterung"),
    ]
    SOMMERUNG_CHOICHES = [
        ("2024 Sommerung", "2024 Sommerung"),
        ("2023 Sommerung", "2023 Sommerung"),
        ("2022 Sommerung", "2022 Sommerung"),
        ("2021 Sommerung", "2021 Sommerung"),
        ("2020 Sommerung", "2020 Sommerung"),
        ("2019 Sommerung", "2019 Sommerung"),
        ("2018 Sommerung", "2018 Sommerung"),
        ("2017 Sommerung", "2017 Sommerung"),
        ("2016 Sommerung", "2016 Sommerung"),
        ("2015 Sommerung", "2015 Sommerung"),
        ("2014 Sommerung", "2014 Sommerung"),
        ("2013 Sommerung", "2013 Sommerung"),
        ("2012 Sommerung", "2012 Sommerung"),
        ("2011 Sommerung", "2011 Sommerung"),
        ("2010 Sommerung", "2010 Sommerung"),
        ("2009 Sommerung", "2009 Sommerung"),
        ("2008 Sommerung", "2008 Sommerung"),
        ("2007 Sommerung", "2007 Sommerung"),
        ("2006 Sommerung", "2006 Sommerung"),
        ("2005 Sommerung", "2005 Sommerung"),
    ]
    PREVIOUS_CHOICES = [
        ('Mais', 'Mais'),
        ('Hanf', 'Hanf'),
        ('Flachs', 'Flachs'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID",
                          help_text="Eindeutige ID der historischen Daten.")
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="historical_data", verbose_name="Schlag *",
                             help_text="Der Schlag, dem diese historischen Daten zugeordnet sind.")
    previous_crop = models.CharField(max_length=100, choices=PREVIOUS_CHOICES, verbose_name="Vorfrucht",
                                     help_text="Welche Vorfrucht wurde auf dem Schlag bereits angebaut?")
    sommerung = models.CharField(max_length=100, choices=SOMMERUNG_CHOICHES, verbose_name="Jahr der Sommerung",
                                 help_text="Nur Ausfüllen, wenn es sich um eine Sommerung handelt.", blank=True,
                                 null=True)
    winterung = models.CharField(max_length=100, choices=WINTERUNG_CHOICES, verbose_name="Jahr der Winterung",
                                 help_text="Nur Ausfüllen, wenn es sich um eine Winterung handelt.", blank=True,
                                 null=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Historische Daten"
        verbose_name_plural = "Historische Daten"

    def __str__(self):
        return f"Historische Daten für {self.plot.name}"


class SoilPreparation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID",
                          help_text="Eindeutige ID der Bodenvorbereitung.")

    INTENSITY_CHOICES = [
        ('flach', 'Flach'),
        ('mittel', 'Mittel'),
        ('tief', 'Tief'),
        ('Minimalvorbereitung', 'Minimalvorbereitung'),
    ]

    TYPE_CHOICES = [
        ('grubbern', 'grubbern'),
        ('eggen', 'eggen'),
        ('pflügen', 'pflügen'),
    ]

    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="soil_preparation", verbose_name="Schlag *",
                             help_text="Der Schlag, für den die Bodenvorbereitung durchgeführt wurde.")
    intensity = models.CharField(max_length=50, choices=INTENSITY_CHOICES, verbose_name="Intensität",
                                 help_text="Die Intensität der Bodenvorbereitung.")
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, verbose_name="Art der Durchführung",
                            help_text="Die Art der durchgeführten Bodenvorbereitung.")
    additional_information = models.TextField(verbose_name="Zusätzliche Ergänzungsparameter",
                                              help_text="", null=True, blank=True)
    created_at = models.DateField(default=now, verbose_name="Datum *")

    class Meta:
        verbose_name = "Prozessdaten 1 - Bodenvorbereitung"
        verbose_name_plural = "Prozessdaten 1 - Bodenvorbereitungen"

    def __str__(self):
        return f"Bodenvorbereitung für {self.plot.name}"


class Fertilization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID",
                          help_text="Eindeutige ID der Düngung.")

    FERTILIZER_CHOICES = [
        ('Stickstoff', 'Stickstoff'),
        ('Phosphor', 'Phosphor'),
        ('Kalk', 'Kalk'),
        ('Kalium', 'Kalium'),
        ('Magnesium', 'Magnesium'),
    ]

    DOSAGEFORM_CHOICES = [
        ('?', '?')
    ]
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="fertilizations", verbose_name="Schlag *",
                             help_text="Der Schlag, für den die Düngung durchgeführt wurde.")
    fertilizer = models.CharField(max_length=50, choices=FERTILIZER_CHOICES, verbose_name="Dünger",
                                  help_text="Der verwendete Dünger (z. B. NPK, Kalk).")
    dosage_form = models.CharField(max_length=50, choices=DOSAGEFORM_CHOICES, verbose_name="Darreichungsform", null=True, blank=True)
    amount = models.IntegerField(verbose_name="Menge (kg/ha)", help_text="Die Düngermenge pro Hektar (kg/ha).")
    created_at = models.DateField(default=now, verbose_name="Datum *",
                                  help_text="Das Datum, an dem die Düngung durchgeführt wurde.")

    class Meta:
        verbose_name = "Prozessdaten 2 - Düngung"
        verbose_name_plural = "Prozessdaten 2 - Düngung"

    def __str__(self):
        return f"Düngung für {self.plot.name} am {self.created_at}"


class Seeding(models.Model):

    VARIETY_CHOICES = [
        ('Hanf', 'Hanf'),
        ('Flachs', 'Flachs'),
    ]

    SORTE_CHOICES = [
        ('Ostara 9', 'Ostara 9'),
        ('Nashinoïde 15', 'Nashinoïde 15'),
        ('Mona 16', 'Mona 16'),
        ('Djumbo 20', 'Djumbo 20'),
        ('Muka 76', 'Muka 76'),
        ('Futura 83', 'Futura 83'),
        ('Santhica 27', 'Santhica 27'),
        ('Futura 75', 'Futura 75'),
        ('Fibror 79', 'Fibror 79'),
        ('Felina 32', 'Felina 32'),
        ('Fedora 17', 'Fedora 17'),
        ('Ferimon', 'Ferimon'),
        ('Earlina 08', 'Earlina 08'),
        ('USO 31', 'USO 31'),
        ('Dioïca 88', 'Dioïca 88'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID",
                          help_text="Eindeutige ID der Aussaat.")
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="seedings", verbose_name="Schlag *",
                             help_text="Der Schlag, für den die Aussaat durchgeführt wurde.")
    variety = models.CharField(max_length=255, choices=VARIETY_CHOICES, verbose_name="Kulturart",
                               help_text="Kulturart (z.B. Hanf, Flachs).")
    sorte = models.CharField(max_length=255, choices=SORTE_CHOICES, verbose_name="Sorte",
                               help_text="", null=True, blank=True)
    seeding_rate = models.FloatField(verbose_name="Ausaatstärke (kg/ha)",
                                       help_text="Die Menge an Saatgut, die pro Hektar ausgesät wurde (in kg/ha).")
    seedbed_width = models.FloatField(default=12.5, verbose_name="Reihenabstand (cm)",
                                        help_text="")
    thousand_grain_weight = models.FloatField( verbose_name="Tausendkorngewicht (g)",
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
    procedure_text = models.TextField(verbose_name="Weitere Erläuterungen zum Prozess",
                                 help_text="", blank=True, null=True)
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
    substance = models.CharField(max_length=255, verbose_name="Handelsname",
                                 help_text="Die verwendete chemische Substanz zur Unkrautbekämpfung.")
    amount = models.IntegerField(verbose_name="Menge (l/ha)",
                                 help_text="Die ausgebrachte Menge der chemischen Substanz.")
    created_at = models.DateField(default=now, verbose_name="Erhebungszeitpunkt",
                                  help_text="Das Datum, an dem die Anwendung der chemischen Unkrautbekämpfung erfasst wurde.")

    class Meta:
        verbose_name = "Bestandspflege - Unkrautbekämpfung - Chemisch"
        verbose_name_plural = "Bestandspflege - Unkrautbekämpfung - Chemisch"


class Harvest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID",
                          help_text="Eindeutige ID der Ernteerfassung.")

    plotpart = models.ForeignKey(PlotParts, on_delete=models.CASCADE, related_name="harvests", verbose_name="Teilschlag *",
                             help_text="Der Teilschlag, für den die Ernte vorgenommen wurde.", null=True, blank=True)
    procedure = models.CharField(max_length=255, verbose_name="Ernte-Prozedur",
                                 help_text="Verfahren, nach dem die Ernte durchgeführt wurde.")
    created_at = models.DateField(default=now, verbose_name="Datum *",
                                  help_text="Das Datum, an dem die Ernte durchgeführt wurde.")

    class Meta:
        verbose_name = "Prozessdaten 7 - Ernteschnitt"
        verbose_name_plural = "Prozessdaten 7 - Ernteschnitt"


class Conditioning(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID",
                          help_text="Eindeutige ID der Konditionierungserfassung.")
    PROCEDURE_CHOICES = [
        ('Wenden', 'Wenden'),
        ('Lüften', 'Lüften'),
    ]
    plotpart = models.ForeignKey(PlotParts, on_delete=models.CASCADE, related_name="conditioning", verbose_name="Teilschlag *",
                             help_text="Der Teilschlag, für den die Ernte vorgenommen wurde.", null=True, blank=True)
    procedure = models.CharField(max_length=20, choices=PROCEDURE_CHOICES, verbose_name="Prozedur",
                                 help_text="Die angewandte Prozedur zur Nachbehandlung des Ernteguts.")
    created_at = models.DateField(default=now, verbose_name="Datum *",
                                  help_text="Das Datum, an dem die Konditionierung durchgeführt wurde.")

    class Meta:
        verbose_name = "Prozessdaten 8 - Konditionierung"
        verbose_name_plural = "Prozessdaten 8 - Konditionierung"


class Bailing(models.Model):
    PROCEDURE_CHOICES = [
        ('Rollen', 'Rollen'),
        ('Pressen', 'Pressen'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    plotpart = models.ForeignKey(PlotParts, on_delete=models.CASCADE, related_name="bailings", verbose_name="Teilschlag *",
                                 blank=True, null=True)
    procedure = models.CharField(max_length=20, choices=PROCEDURE_CHOICES, verbose_name="Prozedur",
                                 help_text="Die angewandte Prozedur zum Ballieren.", blank=True)
    amount = models.IntegerField(default= 0, verbose_name="Anzahl Ballen")
    weight = models.IntegerField(verbose_name="Gewicht", blank=True, help_text="Stichprobenartiges Gewicht.")
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
    stem_thickness= models.IntegerField(verbose_name="Stängeldicke")
    plant_density = models.IntegerField(verbose_name="Pflanzendichte")
    topcut = models.BooleanField(verbose_name="Topcut")
    shoots_number = models.IntegerField(verbose_name="Anzahl Doppeltriebe", null=True, blank=True)
    growth_form = models.IntegerField(choices=PERCENT_CHOICES, verbose_name="Wuchsform", null=True,
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
    cn_ratio = models.CharField(max_length= 255, verbose_name="C/N Verhältnis", help_text="Verhältnis von Kohlenstoff zu Stickstoff",
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

    # Zeitpunkt der Probenahme (not allowed to be empty)
    sampling_date = models.DateField(default=now, verbose_name="Probenahmedatum *", help_text="Datum der Bodenprobenahme")

    class Meta:
        verbose_name = "Verlaufsanalytik - Manuell - Bodenproben"
        verbose_name_plural = "Verlaufsanalytik - Manuell - Bodenproben"

    def __str__(self):
        return f"Bodenprobe {self.id} - {self.plot.name}"
