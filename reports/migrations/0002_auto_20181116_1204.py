# Generated by Django 2.1.3 on 2018-11-16 20:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='report_date',
            field=models.DateField(default=datetime.date(2018, 11, 16)),
        ),
    ]
