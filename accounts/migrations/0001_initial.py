# Generated by Django 4.0.3 on 2022-03-17 04:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('type', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('MANAGER', 'Manager'), ('RIDER', 'Rider'), ('CUSTOMER', 'Customer')], default=[], max_length=22, null=True)),
                ('username', models.CharField(blank=True, max_length=155, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be entred in the format: +8801555555550, Up to 11 digits allowed.', regex='^(((?:\\+88)?(?:\\d{11}))|((?:01)?(?:\\d{11})))$')])),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6, verbose_name='gender')),
                ('address', models.CharField(max_length=50, verbose_name='address')),
                ('otp', models.CharField(blank=True, max_length=6, verbose_name='otp')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('joinded_date', models.DateTimeField(auto_now_add=True, verbose_name='date join')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.location', verbose_name='location')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.account',),
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.account',),
        ),
        migrations.CreateModel(
            name='Rider',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.account',),
        ),
    ]