# Generated by Django 5.0.4 on 2024-04-11 05:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_delivery', '0003_cmd_total_alter_client_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmd',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='test_delivery.client'),
        ),
        migrations.AlterField(
            model_name='cmd',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
