# Generated by Django 5.1.3 on 2025-01-08 08:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hempdata', '0042_alter_soilpreparation_intensity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soilpreparation',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Datum *'),
        ),
        migrations.AlterField(
            model_name='soilpreparation',
            name='intensity',
            field=models.CharField(choices=[('flach', 'Flach'), ('mittel', 'Mittel'), ('tief', 'Tief'), ('Minimalvorbereitung', 'Minimalvorbereitung')], help_text='Die Intensität der Bodenvorbereitung.', max_length=50, verbose_name='Intensität'),
        ),
    ]