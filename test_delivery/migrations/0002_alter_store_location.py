# Generated by Django 5.0.4 on 2024-04-11 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_delivery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='location',
            field=models.IntegerField(null=True),
        ),
    ]
