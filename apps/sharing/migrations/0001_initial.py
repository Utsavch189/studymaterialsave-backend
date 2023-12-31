# Generated by Django 4.2.1 on 2023-11-08 08:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auths', '0008_alter_usermeta_doj'),
        ('sections', '0008_alter_section_created_at'),
        ('posts', '0007_alter_post_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='SharedSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shared_at', models.DateTimeField(default=datetime.datetime(2023, 11, 8, 13, 50, 20, 651461))),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='from_user_section', to='auths.user')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sections.section')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user_section', to='auths.user')),
            ],
        ),
        migrations.CreateModel(
            name='SharedPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shared_at', models.DateTimeField(default=datetime.datetime(2023, 11, 8, 13, 50, 20, 652462))),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='from_user_post', to='auths.user')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user_post', to='auths.user')),
            ],
        ),
    ]
