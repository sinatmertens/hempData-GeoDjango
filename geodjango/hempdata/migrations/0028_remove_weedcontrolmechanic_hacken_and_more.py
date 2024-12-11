# Generated by Django 5.1.3 on 2024-12-11 15:35

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hempdata', '0027_alter_harvest_created_at_alter_harvest_procedure_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weedcontrolmechanic',
            name='hacken',
        ),
        migrations.RemoveField(
            model_name='weedcontrolmechanic',
            name='rollen',
        ),
        migrations.RemoveField(
            model_name='weedcontrolmechanic',
            name='striegeln',
        ),
        migrations.AlterField(
            model_name='conditioning',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now, help_text='Das Datum, an dem die Konditionierung durchgeführt wurde.', verbose_name='Datum'),
        ),
        migrations.AlterField(
            model_name='conditioning',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='Eindeutige ID der Konditionierungserfassung.', primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='conditioning',
            name='plot',
            field=models.ForeignKey(help_text='Der Schlag, in dem die Konditionierungsmaßnahmen durchgeführt wurden.', on_delete=django.db.models.deletion.CASCADE, related_name='conditioning', to='hempdata.plot', verbose_name='Schlag'),
        ),
        migrations.AlterField(
            model_name='conditioning',
            name='procedure',
            field=models.CharField(choices=[('Wenden', 'Wenden'), ('Lüften', 'Lüften')], help_text='Die angewandte Prozedur zur Nachbehandlung des Ernteguts.', max_length=20, verbose_name='Prozedur'),
        ),
        migrations.AlterField(
            model_name='fertilization',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now, help_text='Das Datum, an dem die Düngung durchgeführt wurde.', verbose_name='Datum'),
        ),
        migrations.AlterField(
            model_name='fertilization',
            name='plot',
            field=models.ForeignKey(help_text='Der Schlag, für den die Düngung durchgeführt wurde.', on_delete=django.db.models.deletion.CASCADE, related_name='fertilizations', to='hempdata.plot', verbose_name='Schlag'),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now, help_text='Das Datum, an dem die Ernte durchgeführt wurde.', verbose_name='Datum'),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='Eindeutige ID der Ernteerfassung.', primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='plot',
            field=models.ForeignKey(help_text='Der Schlag, für den die Ernte vorgenommen wurde.', on_delete=django.db.models.deletion.CASCADE, related_name='harvests', to='hempdata.plot', verbose_name='Schlag'),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='procedure',
            field=models.CharField(choices=[('Wirr', 'Wirr'), ('Parallel', 'Parallel')], help_text='Verfahren, nach dem die Ernte durchgeführt wurde.', max_length=20, verbose_name='Ernte-Prozedur'),
        ),
        migrations.AlterField(
            model_name='seeding',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now, help_text='Das Datum, an dem die Aussaat vorgenommen wurde.', verbose_name='Datum'),
        ),
        migrations.AlterField(
            model_name='seeding',
            name='plot',
            field=models.ForeignKey(help_text='Der Schlag, für den die Aussaat durchgeführt wurde.', on_delete=django.db.models.deletion.CASCADE, related_name='seedings', to='hempdata.plot', verbose_name='Schlag'),
        ),
        migrations.AlterField(
            model_name='soilpreparation',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now, help_text='Das Datum, an dem die Düngung durchgeführt wurde.', verbose_name='Datum'),
        ),
        migrations.AlterField(
            model_name='topcut',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now, help_text='Das Datum, an dem der Topcut stattgefunden hat.', verbose_name='Datum'),
        ),
        migrations.AlterField(
            model_name='topcut',
            name='plot',
            field=models.ForeignKey(help_text='Der Schlag, für den der Kopfschnitt durchgeführt wurde.', on_delete=django.db.models.deletion.CASCADE, related_name='topcuts', to='hempdata.plot', verbose_name='Schlag'),
        ),
        migrations.AlterField(
            model_name='weedcontrolchemical',
            name='amount',
            field=models.IntegerField(help_text='Die ausgebrachte Menge der chemischen Substanz.', verbose_name='Menge'),
        ),
        migrations.AlterField(
            model_name='weedcontrolchemical',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now, help_text='Das Datum, an dem die Anwendung der chemischen Unkrautbekämpfung erfasst wurde.', verbose_name='Erhebungszeitpunkt'),
        ),
        migrations.AlterField(
            model_name='weedcontrolchemical',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='Eindeutige ID der chemischen Unkrautbekämpfung.', primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='weedcontrolchemical',
            name='plot',
            field=models.ForeignKey(help_text='Der Schlag, auf dem die chemische Unkrautbekämpfung durchgeführt wurde.', on_delete=django.db.models.deletion.CASCADE, related_name='chemical_weed_controls', to='hempdata.plot', verbose_name='Schlag'),
        ),
        migrations.AlterField(
            model_name='weedcontrolchemical',
            name='substance',
            field=models.CharField(help_text='Die verwendete chemische Substanz zur Unkrautbekämpfung.', max_length=255, verbose_name='Substanz'),
        ),
        migrations.AlterField(
            model_name='weedcontrolmechanic',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now, help_text='Das Datum, an dem die Unkrautbekämpfung vorgenommen wurde.', verbose_name='Datum'),
        ),
        migrations.AlterField(
            model_name='weedcontrolmechanic',
            name='plot',
            field=models.ForeignKey(help_text='Der Schlag, für den die mechanische Unkrautbekämpfung durchgeführt wurde.', on_delete=django.db.models.deletion.CASCADE, related_name='mechanic_weed_controls', to='hempdata.plot', verbose_name='Schlag'),
        ),
    ]