# Generated by Django 5.1.3 on 2025-01-08 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hempdata', '0046_seeding_sorte_alter_seeding_seedbed_width_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seeding',
            name='seedbed_width',
            field=models.FloatField(default=12.5, verbose_name='Reihenabstand (cm)'),
        ),
        migrations.AlterField(
            model_name='seeding',
            name='seeding_rate',
            field=models.FloatField(help_text='Die Menge an Saatgut, die pro Hektar ausgesät wurde (in kg/ha).', verbose_name='Ausaatstärke (kg/ha)'),
        ),
    ]
