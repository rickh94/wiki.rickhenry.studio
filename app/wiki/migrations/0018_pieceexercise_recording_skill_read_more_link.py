# Generated by Django 4.2.5 on 2023-09-19 18:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wiki", "0017_alter_pieceexercise_piece"),
    ]

    operations = [
        migrations.AddField(
            model_name="pieceexercise",
            name="recording",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="wiki.recording",
            ),
        ),
        migrations.AddField(
            model_name="skill",
            name="read_more_link",
            field=models.URLField(blank=True, null=True),
        ),
    ]