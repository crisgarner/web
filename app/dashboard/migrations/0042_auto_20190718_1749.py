# Generated by Django 2.1.7 on 2019-07-18 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0041_auto_20190718_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='bounty',
            name='last_remarketed',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='bounty',
            name='remarketed_count',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
    ]