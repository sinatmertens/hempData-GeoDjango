# Generated by Django 5.1.3 on 2025-01-07 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hempdata', '0034_alter_historicaldata_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaldata',
            name='season',
            field=models.CharField(choices=[('Sommerung', 'Sommerung'), ('Winterung', 'Winterung')], max_length=10, null=True, verbose_name='Sommerung/Winterung'),
        ),
        migrations.AlterField(
            model_name='historicaldata',
            name='created_at',
            field=models.DateField(help_text='Das ungefähre Datum.', verbose_name='Erhebungszeitpunkt'),
        ),
        migrations.AlterField(
            model_name='historicaldata',
            name='previous_crop',
            field=models.CharField(help_text='Welche Vorfrucht wurde auf dem Schlag bereits angebaut?', max_length=255, verbose_name='Vorfrucht'),
        ),
    ]