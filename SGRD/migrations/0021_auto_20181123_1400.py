# Generated by Django 2.1.3 on 2018-11-23 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SGRD', '0020_auto_20181123_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archivo',
            name='descarga_archivo',
        ),
        migrations.AddField(
            model_name='descargararchivo',
            name='archivo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='SGRD.Archivo'),
        ),
    ]
