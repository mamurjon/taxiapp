# Generated by Django 2.0.1 on 2018-01-31 08:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mytaxiapp', '0002_user_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('start_place', models.CharField(max_length=127)),
                ('finish_place', models.CharField(max_length=127)),
                ('pickup_date', models.DateField(blank=True, null=True)),
                ('pickup_time', models.TimeField(blank=True, null=True)),
                ('offer_price', models.CharField(blank=True, max_length=63, null=True)),
                ('status', models.CharField(choices=[('new', 'new'), ('accepted_by_driver', 'accepted_by_driver'), ('driver_came', 'driver_came'), ('customer_in_the_car', 'customer_in_the_car'), ('completed', 'completed')], default='new', max_length=15)),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offer_driver', to='mytaxiapp.Driver')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offer_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]