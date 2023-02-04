# Generated by Django 4.0.5 on 2023-01-27 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('createcontent', '0013_post_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoPOST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='comment',
        ),
        migrations.AddField(
            model_name='post',
            name='commentCounter',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AddField(
            model_name='dopost',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='createcontent.post'),
        ),
    ]