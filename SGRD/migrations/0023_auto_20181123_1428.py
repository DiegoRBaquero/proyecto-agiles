# Generated by Django 2.1.3 on 2018-11-23 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SGRD', '0022_auto_20181123_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descargararchivo',
            name='archivo',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='descarga', to='SGRD.Archivo'),
        ),
    ]
