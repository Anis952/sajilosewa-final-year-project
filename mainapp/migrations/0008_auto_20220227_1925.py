# Generated by Django 3.1.3 on 2022-02-27 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20220219_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='distance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
