# Generated by Django 5.1.3 on 2024-12-06 13:04

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hempdata', '0016_historicaldata_unique_plot_historical_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bailing',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Erhebungszeitpunkt'),
        ),
        migrations.AlterField(
            model_name='bailing',
            name='plot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bailings', to='hempdata.plot', verbose_name='Schlag'),
        ),
        migrations.AlterField(
            model_name='bailing',
            name='weight',
            field=models.IntegerField(verbose_name='Gewicht'),
        ),
        migrations.AlterField(
            model_name='conditioning',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Erhebungszeitpunkt'),
        ),
        migrations.AlterField(
            model_name='conditioning',
            name='plot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conditioning', to='hempdata.plot', verbose_name='Schlag'),
        ),
        migrations.AlterField(
            model_name='conditioning',
            name='procedure',
            field=models.CharField(choices=[('Wenden', 'Wenden'), ('Lüften', 'Lüften')], max_length=20, verbose_name='Prozedur'),
        ),
        migrations.AlterField(
            model_name='fertilization',
            name='plot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fertilizations', to='hempdata.plot', verbose_name='Schlag'),
        ),
        migrations.AlterField(
            model_name='field',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Erhebungszeitpunkt'),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Erhebungszeitpunkt'),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='plot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='harvests', to='hempdata.plot', verbose_name='Schlag'),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='procedure',
            field=models.CharField(choices=[('Wirr', 'Wirr'), ('Parallel', 'Parallel')], max_length=20, verbose_name='Prozedur'),
        ),
        migrations.AlterField(
            model_name='historicaldata',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Erhebungszeitpunkt'),
        ),
        migrations.AlterField(
            model_name='plantcharacteristicsbase',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Erhebungszeitpunkt'),
        ),
        migrations.AlterField(
            model_name='plantcharacteristicstop',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Erhebungszeitpunkt'),
        ),
        migrations.AlterField(
            model_name='plot',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Erhebungszeitpunkt'),
        ),
        migrations.AlterField(
            model_name='seeding',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Erhebungszeitpunkt'),
        ),
        migrations.AlterField(
            model_name='seeding',
            name='plot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seedings', to='hempdata.plot', verbose_name='Schlag'),
        ),
        migrations.AlterField(
            model_name='seeding',
            name='seedbed_width',
            field=models.IntegerField(verbose_name='Tausendkorngewicht (kg)'),
        ),
        migrations.AlterField(
            model_name='seeding',
            name='seeding_rate',
            field=models.IntegerField(verbose_name='Ausaatstärke (kg/ha)'),
        ),
        migrations.AlterField(
            model_name='seeding',
            name='thousand_grain_weight',
            field=models.FloatField(default=12.5, verbose_name='•\tSaatbettreite (cm)'),
        ),
        migrations.AlterField(
            model_name='seeding',
            name='variety',
            field=models.CharField(max_length=255, verbose_name='Kulturart'),
        ),
        migrations.AlterField(
            model_name='soilpreparation',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Erhebungszeitpunkt'),
        ),
        migrations.AlterField(
            model_name='topcut',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Erhebungszeitpunkt'),
        ),
        migrations.AlterField(
            model_name='topcut',
            name='cutting_height',
            field=models.IntegerField(verbose_name='Schnitthöhe'),
        ),
        migrations.AlterField(
            model_name='topcut',
            name='plot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topcuts', to='hempdata.plot', verbose_name='Schlag'),
        ),
        migrations.AlterField(
            model_name='weatherstation',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='Standort'),
        ),
        migrations.AlterField(
            model_name='weedcontrolchemical',
            name='amount',
            field=models.IntegerField(verbose_name='Menge'),
        ),
        migrations.AlterField(
            model_name='weedcontrolchemical',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Erhebungszeitpunkt'),
        ),
        migrations.AlterField(
            model_name='weedcontrolchemical',
            name='plot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chemical_weed_controls', to='hempdata.plot', verbose_name='Schlag'),
        ),
        migrations.AlterField(
            model_name='weedcontrolchemical',
            name='substance',
            field=models.CharField(max_length=255, verbose_name='Substanz'),
        ),
        migrations.AlterField(
            model_name='weedcontrolmechanic',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Erhebungszeitpunkt'),
        ),
        migrations.AlterField(
            model_name='weedcontrolmechanic',
            name='emergence',
            field=models.CharField(choices=[('Nach dem Auflauf', 'Nach dem Auflauf'), ('Vor dem Auflauf', 'Vor dem Auflauf')], max_length=20, verbose_name='Nach/Vor dem Auflauf'),
        ),
        migrations.AlterField(
            model_name='weedcontrolmechanic',
            name='hacken',
            field=models.BooleanField(default=False, verbose_name='Hacken'),
        ),
        migrations.AlterField(
            model_name='weedcontrolmechanic',
            name='plot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mechanic_weed_controls', to='hempdata.plot', verbose_name='Schlag'),
        ),
        migrations.AlterField(
            model_name='weedcontrolmechanic',
            name='rollen',
            field=models.BooleanField(default=False, verbose_name='Rollen'),
        ),
        migrations.AlterField(
            model_name='weedcontrolmechanic',
            name='striegeln',
            field=models.BooleanField(default=False, verbose_name='Striegeln'),
        ),
    ]
