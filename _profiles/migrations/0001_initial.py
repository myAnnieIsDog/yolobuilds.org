# Generated by Django 5.0.1 on 2024-08-02 21:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CertificateType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency', models.CharField(max_length=15, unique=True, verbose_name='Agency Acronym')),
                ('agency_long', models.CharField(max_length=255, unique=True, verbose_name='Agency Full Name')),
                ('cert', models.CharField(max_length=7, unique=True, verbose_name='Cert. Code')),
                ('cert_long', models.CharField(max_length=255, unique=True, verbose_name='Certification Type')),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Certification Type',
                'verbose_name_plural': 'Certification Types',
                'ordering': ['cert'],
            },
        ),
        migrations.CreateModel(
            name='ContactType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=55)),
                ('description', models.TextField(max_length=255)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Contact Type',
                'verbose_name_plural': 'Contacts Types',
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=25, unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Yolo Department',
                'verbose_name_plural': 'Yolo Department Options',
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('dba', models.CharField(max_length=55, unique=True)),
                ('prefix', models.CharField(max_length=5, unique=True)),
                ('year', models.CharField(default='2024', max_length=4)),
                ('sequence', models.CharField(default='0001', max_length=12)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Yolo DCS Division',
                'verbose_name_plural': 'Yolo DCS Divisions',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=255)),
                ('first', models.CharField(blank=True, max_length=255, verbose_name='First Name')),
                ('last', models.CharField(blank=True, max_length=255, verbose_name='Last Name')),
                ('company', models.CharField(blank=True, max_length=255, verbose_name='Company Name')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=255)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('state', models.CharField(blank=True, max_length=2)),
                ('zip', models.CharField(blank=True, max_length=10)),
                ('reviewer', models.BooleanField(default=False)),
                ('inspector', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('user_link', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['first', 'last'],
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(max_length=255)),
                ('contact_type', models.CharField(max_length=255)),
                ('profile_link', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='_profiles.profile')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
                'ordering': ['profile'],
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cert_holder', models.CharField(max_length=255)),
                ('cert_type', models.CharField(max_length=255)),
                ('cert_number', models.CharField(max_length=255)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('verified_valid', models.DateField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('cert_holder_link', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='_profiles.profile')),
            ],
            options={
                'verbose_name': 'Certificate',
                'verbose_name_plural': 'Certificates',
                'ordering': ['cert_holder', 'cert_type'],
            },
        ),
        migrations.CreateModel(
            name='AngencyPartners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(blank=True, max_length=255, null=True)),
                ('agency', models.CharField(blank=True, max_length=25, null=True, verbose_name='Agency Nickname')),
                ('full_agency', models.CharField(blank=True, max_length=255, null=True, verbose_name='Agency Full Name')),
                ('alt_contact_name', models.CharField(blank=True, max_length=255, null=True)),
                ('alt_contact_email', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_link', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='_profiles.profile')),
            ],
            options={
                'verbose_name': 'Yolo DCS Partner',
                'verbose_name_plural': 'Yolo DCS Partners',
                'ordering': ['agency', 'profile'],
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(blank=True, max_length=255)),
                ('department', models.CharField(blank=True, max_length=255)),
                ('division', models.CharField(blank=True, max_length=255)),
                ('supervisor', models.CharField(blank=True, max_length=255)),
                ('supervisor_email', models.CharField(blank=True, max_length=255)),
                ('profile_link', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='_profiles.profile')),
            ],
            options={
                'verbose_name': 'Yolo DCS Employee',
                'verbose_name_plural': 'Yolo DCS Employees',
                'ordering': ['department', 'division', 'profile'],
            },
        ),
    ]