# Generated by Django 2.0 on 2018-05-06 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0007_auto_20180505_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='beat',
            name='producer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='beats.Producer'),
        ),
    ]
