# Generated by Django 2.0.1 on 2018-01-31 06:09

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import utils.filename


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('phone_number', models.CharField(max_length=64, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('year_of_birth', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('car_number', models.CharField(blank=True, max_length=63, null=True)),
                ('car_photo', models.ImageField(blank=True, null=True, upload_to=utils.filename.RandomFileName('cars'))),
                ('brand', models.CharField(blank=True, max_length=300, null=True, verbose_name='Car Firm')),
                ('model', models.CharField(blank=True, max_length=300, null=True)),
                ('seats', models.SmallIntegerField(blank=True, default=4)),
                ('color', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('gender', models.CharField(blank=True, max_length=20, null=True)),
                ('biography', models.TextField(blank=True, null=True)),
                ('experience', models.CharField(blank=True, max_length=256, null=True)),
                ('driver_photo', models.ImageField(blank=True, null=True, upload_to=utils.filename.RandomFileName('users'))),
                ('rating', models.DecimalField(decimal_places=1, default=Decimal('0.0'), max_digits=2)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver', to='mytaxiapp.Car')),
            ],
            options={
                'abstract': False,
            },
            bases=('mytaxiapp.user',),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
