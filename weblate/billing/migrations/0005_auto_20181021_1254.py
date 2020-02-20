# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-10-21 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("billing", "0004_auto_20181021_1249")]

    operations = [
        migrations.AlterField(
            model_name="billing",
            name="state",
            field=models.IntegerField(
                choices=[
                    (0, "Active"),
                    (1, "Trial"),
                    (2, "Expired"),
                    (3, "Not activated"),
                ],
                default=0,
                verbose_name="Billing state",
            ),
        )
    ]
