# Generated by Django 2.1.2 on 2018-11-12 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGRD', '0015_merge_20181103_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etiqueta',
            name='color',
            field=models.CharField(default='79ADDC', max_length=7),
        ),
    ]
