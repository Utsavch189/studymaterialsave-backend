# Generated by Django 4.2.6 on 2023-10-28 16:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 28, 21, 43, 46, 949662)),
        ),
    ]