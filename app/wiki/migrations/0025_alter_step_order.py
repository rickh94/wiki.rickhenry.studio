# Generated by Django 4.2.5 on 2023-09-20 18:10

import wiki.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wiki", "0024_alter_spot_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="step",
            name="order",
            field=models.IntegerField(validators=[wiki.models.validate_positive]),
        ),
    ]
