# Generated by Django 4.2.1 on 2023-11-05 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0003_alter_usermeta_doj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermeta',
            name='doj',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 5, 18, 35, 42, 581922)),
        ),
    ]
