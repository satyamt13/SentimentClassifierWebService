# Generated by Django 3.0.6 on 2020-05-27 05:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0002_mlalgorithm_mlalgorithmstatus_mlrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='mlalgorithm',
            name='owner',
            field=models.CharField(default=django.utils.timezone.now, max_length=128),
            preserve_default=False,
        ),
    ]
