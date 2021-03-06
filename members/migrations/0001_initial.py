# Generated by Django 2.1.3 on 2018-11-16 03:37

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_number', models.CharField(max_length=4, unique=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator('^[1-9][0-9]*$', 'Must be numeric and cannot begin with zero.')], verbose_name='Member Number')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('gender', models.CharField(choices=[('Girl', 'Girl'), ('Boy', 'Boy')], default=None, max_length=4, verbose_name='Gender')),
                ('birth_date', models.DateField(default=datetime.date(2018, 11, 15))),
            ],
        ),
    ]
