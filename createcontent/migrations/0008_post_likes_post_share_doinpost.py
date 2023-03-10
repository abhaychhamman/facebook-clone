# Generated by Django 4.0.5 on 2023-01-26 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('createcontent', '0007_alter_friendsmodal_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='share',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.CreateModel(
            name='DoInPOST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=50)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
