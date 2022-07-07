# Generated by Django 4.0.5 on 2022-07-07 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('branch_name', models.CharField(db_index=True, max_length=150)),
                ('phone_number', models.CharField(db_index=True, max_length=15)),
                ('address', models.TextField(max_length=200)),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='name')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tracking_id', models.CharField(blank=True, db_index=True, max_length=12, unique=True, verbose_name='tracking id')),
                ('customer_name', models.CharField(max_length=100, verbose_name='customer name')),
                ('customer_phone_number', models.CharField(db_index=True, max_length=100, verbose_name='customer phone number')),
                ('customer_address', models.CharField(max_length=250, verbose_name='customer address')),
                ('parcel_weight', models.CharField(default='500gm', max_length=10, verbose_name='parcel weight')),
                ('product_selling_price', models.CharField(max_length=15, verbose_name='product selling price')),
                ('product_category', models.CharField(max_length=100, verbose_name='product category')),
                ('description', models.TextField(max_length=350, verbose_name='description')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Completed', 'Completed'), ('Cancel', 'Cancel')], db_index=True, default='Pending', max_length=15, verbose_name='status')),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ParcelDelivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Accept', 'Accept'), ('Pending', 'Pending'), ('Delivered', 'Delivered')], db_index=True, default='Pending', max_length=9)),
            ],
            options={
                'verbose_name': 'Parcel Delivery',
                'verbose_name_plural': 'Parcel Deliveries',
            },
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('truck_diver_name', models.CharField(max_length=50)),
                ('truck_diver_phone_number', models.CharField(db_index=True, max_length=15)),
                ('truck_plate_number', models.CharField(db_index=True, max_length=50)),
                ('status', models.CharField(choices=[('Accept', 'Accept'), ('Pending', 'Pending'), ('SC', 'Shipment Completed'), ('Return', 'Return')], db_index=True, default='Pending', max_length=10)),
                ('parcel', models.ManyToManyField(to='delivery_managements.parcel')),
                ('receiver_branch', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shipment_receiver_branch', to='delivery_managements.branch')),
                ('sender_branch', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shipment_sender_branch', to='delivery_managements.branch')),
                ('shipment_to', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shipments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PickupLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pickup_name', models.CharField(max_length=150, verbose_name='picup name')),
                ('pickup_address', models.CharField(max_length=250, verbose_name='picup address')),
                ('pickup_phone_number', models.CharField(db_index=True, max_length=50, verbose_name='pickup phone number')),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='delivery_managements.branch')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pickup_location', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'pickup location',
                'verbose_name_plural': 'pickup locations',
            },
        ),
        migrations.CreateModel(
            name='ParcelPickup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Accept', 'Accept'), ('Pending', 'Pending'), ('PC', 'Pickup Complete')], db_index=True, default='Pending', max_length=9)),
                ('parcel', models.ManyToManyField(related_name='parcel_pickup', to='delivery_managements.parcel')),
            ],
            options={
                'verbose_name': 'Parcel Pickup',
                'verbose_name_plural': 'Parcel Pickup',
            },
        ),
    ]
