# Generated by Django 2.1.4 on 2018-12-26 17:16

from django.db import migrations, models
import django.db.models.deletion
import economy.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ENSSubdomainRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('subdomain_wallet_address', models.CharField(max_length=50)),
                ('txn_hash_1', models.CharField(blank=True, max_length=255)),
                ('txn_hash_2', models.CharField(blank=True, max_length=255)),
                ('txn_hash_3', models.CharField(blank=True, max_length=255)),
                ('pending', models.BooleanField()),
                ('signed_msg', models.TextField()),
                ('start_nonce', models.IntegerField(default=0)),
                ('end_nonce', models.IntegerField(default=0)),
                ('gas_cost_eth', models.FloatField(default=0.000649197)),
                ('comments', models.TextField(blank=True)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ens_registration', to='dashboard.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
