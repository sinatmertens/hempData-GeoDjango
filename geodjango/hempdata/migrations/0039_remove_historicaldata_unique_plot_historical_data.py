# Generated by Django 5.1.3 on 2025-01-07 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hempdata', '0038_alter_historicaldata_sommerung_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='historicaldata',
            name='unique_plot_historical_data',
        ),
    ]
