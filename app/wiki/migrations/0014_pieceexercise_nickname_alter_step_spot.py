# Generated by Django 4.2.5 on 2023-09-17 20:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wiki", "0013_spot_nickname"),
    ]

    operations = [
        migrations.AddField(
            model_name="pieceexercise",
            name="nickname",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="step",
            name="spot",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="steps",
                to="wiki.spot",
            ),
        ),
    ]
