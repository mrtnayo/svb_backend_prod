# Generated by Django 3.0.7 on 2020-07-15 03:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(choices=[(1, 'Casa'), (2, 'Oficina'), (0, 'Otros')], default=1, max_length=1)),
                ('street_address', models.CharField(max_length=128)),
                ('apartment_address', models.CharField(blank=True, max_length=128, null=True)),
                ('zip', models.CharField(max_length=5)),
                ('default', models.BooleanField(default=False)),
                ('ubigeo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.Ubigeo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('document_type', models.CharField(blank=True, choices=[('00', 'OTROS'), ('01', 'L.E. / DNI'), ('04', 'CARNET EXT.'), ('06', 'RUC'), ('07', 'PASAPORTE'), ('11', 'P. NAC.')], default='01', help_text='Tipo de documento', max_length=2, null=True, verbose_name='Document Type')),
                ('document_number', models.CharField(blank=True, help_text='Número de documento', max_length=15, null=True, verbose_name='Document Number')),
                ('first_name', models.CharField(blank=True, help_text='Nombres', max_length=50, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, help_text='Apellidos', max_length=50, null=True, verbose_name='Last Name')),
                ('birthdate', models.DateField(blank=True, help_text='Fecha de nacimiento', null=True, verbose_name='Birthdate')),
                ('mobile_phone_number', models.CharField(blank=True, help_text='Número de celular', max_length=15, null=True, verbose_name='Mobile phone number')),
                ('home_phone_number', models.CharField(blank=True, help_text='Número de teléfono casa', max_length=15, null=True, verbose_name='Home phone number')),
                ('work_phone_number', models.CharField(blank=True, help_text='Número de oficina o centro de trabajo', max_length=15, null=True, verbose_name='Work phone number')),
                ('nationality', models.CharField(blank=True, help_text='Nacionalidad', max_length=30, null=True, verbose_name='Nationality')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('billing_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rest_auth.Address')),
            ],
            options={
                'abstract': False,
                'unique_together': {('document_type', 'document_number')},
            },
        ),
    ]
