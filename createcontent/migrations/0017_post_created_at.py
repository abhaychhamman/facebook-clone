# Generated by Django 4.0.5 on 2023-01-28 22:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createcontent', '0016_alter_dopost_commentsusername'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
