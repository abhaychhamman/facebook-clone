# Generated by Django 4.0.5 on 2023-01-25 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_profile_email'),
        ('createcontent', '0006_alter_friendsmodal_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendsmodal',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.profile'),
        ),
    ]
