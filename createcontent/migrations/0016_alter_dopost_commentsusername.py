# Generated by Django 4.0.5 on 2023-01-28 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createcontent', '0015_dopost_commentsusername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dopost',
            name='commentsUsername',
            field=models.CharField(default='admin', max_length=50),
        ),
    ]