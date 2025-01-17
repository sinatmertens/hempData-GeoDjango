# Generated by Django 5.1.3 on 2025-01-09 09:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hempdata', '0048_plotparts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='harvest',
            options={'verbose_name': 'Prozessdaten 7 - Ernteschnitt', 'verbose_name_plural': 'Prozessdaten 7 - Ernteschnitt'},
        ),
        migrations.RemoveField(
            model_name='harvest',
            name='plot',
        ),
        migrations.AddField(
            model_name='harvest',
            name='plotpart',
            field=models.ForeignKey(blank=True, help_text='Der Teilschlag, für den die Ernte vorgenommen wurde.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='harvests', to='hempdata.plotparts', verbose_name='Teilschlag *'),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='procedure',
            field=models.CharField(help_text='Verfahren, nach dem die Ernte durchgeführt wurde.', max_length=255, verbose_name='Ernte-Prozedur'),
        ),
    ]
