# Generated by Django 4.2.1 on 2023-11-08 08:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0007_alter_usermeta_doj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermeta',
            name='doj',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 8, 13, 50, 20, 629462)),
        ),
    ]