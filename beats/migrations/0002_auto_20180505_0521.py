# Generated by Django 2.0 on 2018-05-05 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beat',
            name='playback',
            field=models.FileField(upload_to=''),
        ),
    ]