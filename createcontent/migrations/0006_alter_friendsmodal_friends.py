# Generated by Django 4.0.5 on 2023-01-25 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createcontent', '0005_remove_friendsmodal_friendreqsendto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendsmodal',
            name='friends',
            field=models.ManyToManyField(blank=True, to='createcontent.friendsmodal'),
        ),
    ]
