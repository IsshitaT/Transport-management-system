# Generated by Django 3.1.3 on 2020-11-15 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import transportapp.storages


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TruckMaintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('truckno', models.CharField(default=None, max_length=100)),
                ('service_date', models.DateField()),
                ('service_km', models.FloatField()),
                ('service_details', models.CharField(max_length=1000)),
                ('service_by', models.CharField(max_length=200)),
                ('service_cost', models.FloatField()),
                ('service_note', models.CharField(blank=True, max_length=500, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Loan_Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('truckno', models.CharField(default=None, max_length=15)),
                ('owner_name', models.CharField(max_length=50)),
                ('loan_amount', models.FloatField()),
                ('interest_rate', models.FloatField()),
                ('loan_duration', models.IntegerField()),
                ('installment_amount', models.FloatField(null=True)),
                ('installment_date', models.DateField()),
                ('month_paid', models.IntegerField(blank=True, default=0)),
                ('months', models.IntegerField(blank=True, null=True)),
                ('inlineRadioOptions', models.CharField(blank=True, max_length=5, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('truckno', models.CharField(default=None, max_length=100)),
                ('puc', models.FileField(blank=True, default=None, null=True, storage=transportapp.storages.OverwriteStorage(), upload_to='docs/')),
                ('insurance', models.FileField(blank=True, default=None, null=True, storage=transportapp.storages.OverwriteStorage(), upload_to='docs/')),
                ('rc', models.FileField(blank=True, default=None, null=True, storage=transportapp.storages.OverwriteStorage(), upload_to='docs/')),
                ('india_permit', models.FileField(blank=True, default=None, null=True, storage=transportapp.storages.OverwriteStorage(), upload_to='docs/')),
                ('state_permit', models.FileField(blank=True, default=None, null=True, storage=transportapp.storages.OverwriteStorage(), upload_to='docs/')),
                ('fitness', models.FileField(blank=True, default=None, null=True, storage=transportapp.storages.OverwriteStorage(), upload_to='docs/')),
                ('decleration', models.FileField(blank=True, default=None, null=True, storage=transportapp.storages.OverwriteStorage(), upload_to='docs/')),
                ('danda', models.FileField(default=None, storage=transportapp.storages.OverwriteStorage(), upload_to='docs/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cashbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cashbook_date', models.DateField()),
                ('particular', models.CharField(max_length=50)),
                ('cashbook_amount', models.IntegerField()),
                ('transection_type', models.CharField(default=None, max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bilty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mob', models.CharField(blank=True, max_length=10, null=True)),
                ('invoiceno', models.CharField(max_length=20)),
                ('truckno', models.CharField(default=None, max_length=100)),
                ('date', models.DateField()),
                ('consignor_details', models.CharField(max_length=500)),
                ('consignee_details', models.CharField(max_length=500)),
                ('lr_no', models.IntegerField()),
                ('rate', models.FloatField()),
                ('weight', models.FloatField()),
                ('fair', models.FloatField()),
                ('advance', models.IntegerField()),
                ('recived_money', models.IntegerField()),
                ('goods_description', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
