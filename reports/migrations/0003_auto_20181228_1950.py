# Generated by Django 2.1.3 on 2018-12-29 03:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20181116_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='report_date',
            field=models.DateField(default=datetime.date(2018, 12, 28)),
        ),
    ]
