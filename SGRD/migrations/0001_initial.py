# Generated by Django 2.1.1 on 2018-09-30 23:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('ruta', models.FileField(upload_to='archivos_recursos/')),
                ('fecha_creacion', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='EntradaPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField()),
                ('hora', models.TimeField()),
                ('lugar', models.TextField()),
                ('personas', models.TextField()),
                ('equipos', models.TextField()),
                ('descripcion', models.TextField()),
                ('observaciones', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PlanProduccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('proyecto', models.CharField(max_length=200)),
                ('fase', models.CharField(choices=[('A', 'Pre-Producción'), ('B', 'Producción'), ('C', 'Pos-Producción'), ('D', 'Control calidad'), ('E', 'Cierre proyecto'), ('F', 'Sistematización y resguardo')], max_length=1)),
                ('fecha_creacion', models.DateField(blank=True, default=datetime.datetime.now)),
                ('ruta_compartida', models.CharField(max_length=250)),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Tipos',
            },
        ),
        migrations.AddField(
            model_name='recurso',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SGRD.Tipo'),
        ),
        migrations.AddField(
            model_name='planproduccion',
            name='recurso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SGRD.Recurso'),
        ),
        migrations.AddField(
            model_name='entradaplan',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SGRD.PlanProduccion'),
        ),
        migrations.AddField(
            model_name='archivo',
            name='recurso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SGRD.Recurso'),
        ),
    ]
