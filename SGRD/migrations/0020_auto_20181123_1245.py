# Generated by Django 2.1.3 on 2018-11-23 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SGRD', '0019_auto_20181118_2219'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archivo',
            options={'ordering': ['-fecha_creacion']},
        ),
    ]
