# Generated by Django 5.0.6 on 2024-05-10 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('option', '0003_postoption_postoptionvalue'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='is_filter',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='option',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]