# Generated by Django 4.2.1 on 2023-11-08 13:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharing', '0004_alter_sharedpost_shared_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sharedpost',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sharedsection',
            name='id',
        ),
        migrations.AddField(
            model_name='sharedpost',
            name='share_id',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='sharedsection',
            name='share_id',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sharedpost',
            name='shared_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 8, 19, 0, 51, 361731)),
        ),
        migrations.AlterField(
            model_name='sharedsection',
            name='shared_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 8, 19, 0, 51, 360733)),
        ),
    ]
