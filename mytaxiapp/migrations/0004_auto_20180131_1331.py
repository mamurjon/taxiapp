# Generated by Django 2.0.1 on 2018-01-31 08:31

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytaxiapp', '0003_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='location_from',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='offer',
            name='location_to',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326),
        ),
    ]
