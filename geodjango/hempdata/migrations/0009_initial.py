# Generated by Django 5.1.3 on 2024-12-03 16:12

import django.contrib.gis.db.models.fields
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hempdata', '0008_remove_conditioning_plot_remove_fertilization_plot_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('size', models.IntegerField()),
                ('location', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('location', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plots', to='hempdata.field')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('previous_crop1', models.CharField(max_length=255)),
                ('previous_crop2', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('plot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historical_data', to='hempdata.plot')),
            ],
        ),
        migrations.CreateModel(
            name='Harvest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('procedure', models.CharField(choices=[('Wirr', 'Wirr'), ('Parallel', 'Parallel')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('plot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='harvests', to='hempdata.plot')),
            ],
        ),
        migrations.CreateModel(
            name='Fertilization',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=True)),
                ('fertilizer', models.CharField(choices=[('type1', 'Type 1'), ('type2', 'Type 2'), ('type3', 'Type 3')], max_length=50)),
                ('amount', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('plot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fertilizations', to='hempdata.plot')),
            ],
        ),
        migrations.CreateModel(
            name='Conditioning',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('procedure', models.CharField(choices=[('Wenden', 'Wenden'), ('Lüften', 'Lüften')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('plot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conditionings', to='hempdata.plot')),
            ],
        ),
        migrations.CreateModel(
            name='Bailing',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('plot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bailings', to='hempdata.plot')),
            ],
        ),
        migrations.CreateModel(
            name='Seeding',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('variety', models.CharField(max_length=255)),
                ('seeding_rate', models.IntegerField()),
                ('seedbed_width', models.IntegerField()),
                ('thousand_grain_weight', models.FloatField(default=12.5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('plot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seedings', to='hempdata.plot')),
            ],
        ),
        migrations.CreateModel(
            name='SoilPreparation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=True)),
                ('intensity', models.CharField(choices=[('flach', 'Flach'), ('mittel', 'Mittel'), ('tief', 'Tief')], max_length=10)),
                ('type', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('plot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='soil_preparations', to='hempdata.plot')),
            ],
        ),
        migrations.CreateModel(
            name='TopCut',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('cutting_height', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('plot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topcuts', to='hempdata.plot')),
            ],
        ),
        migrations.CreateModel(
            name='WeedControlChemical',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('substance', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('plot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chemical_weed_controls', to='hempdata.plot')),
            ],
        ),
        migrations.CreateModel(
            name='WeedControlMechanic',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('hacken', models.BooleanField(default=False)),
                ('striegeln', models.BooleanField(default=False)),
                ('rollen', models.BooleanField(default=False)),
                ('emergence', models.CharField(choices=[('Nach dem Auflauf', 'Nach dem Auflauf'), ('Vor dem Auflauf', 'Vor dem Auflauf')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('plot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mechanic_weed_controls', to='hempdata.plot')),
            ],
        ),
    ]
