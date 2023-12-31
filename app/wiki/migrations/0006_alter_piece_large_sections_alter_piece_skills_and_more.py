# Generated by Django 4.2.5 on 2023-09-09 06:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wiki", "0005_alter_book_description_alter_piece_book_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="piece",
            name="large_sections",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="piece",
            name="skills",
            field=models.ManyToManyField(blank=True, null=True, to="wiki.skill"),
        ),
        migrations.AlterField(
            model_name="spot",
            name="piece",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="spots",
                to="wiki.piece",
            ),
        ),
    ]
