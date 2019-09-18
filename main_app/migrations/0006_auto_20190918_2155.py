# Generated by Django 2.2.5 on 2019-09-18 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_playlist_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.Profile'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='track',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.Track'),
        ),
    ]
