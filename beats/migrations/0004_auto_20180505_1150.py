# Generated by Django 2.0 on 2018-05-05 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0003_auto_20180505_1149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beat',
            old_name='category',
            new_name='genre',
        ),
    ]
