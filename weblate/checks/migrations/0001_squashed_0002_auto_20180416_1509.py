# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-21 12:48

import django.db.models.deletion
from django.db import migrations, models

from weblate.checks import CHECKS


class Migration(migrations.Migration):

    replaces = [("checks", "0001_initial"), ("checks", "0002_auto_20180416_1509")]

    initial = True

    dependencies = [
        ("lang", "0011_auto_20180215_1158"),
        ("trans", "0130_auto_20180416_1503"),
    ]

    operations = [
        migrations.CreateModel(
            name="Check",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content_hash", models.BigIntegerField()),
                (
                    "check",
                    models.CharField(choices=CHECKS.get_choices(), max_length=50),
                ),
                ("ignore", models.BooleanField(db_index=True, default=False)),
                (
                    "language",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lang.Language",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="trans.Project"
                    ),
                ),
            ],
        ),
        migrations.AlterUniqueTogether(
            name="check",
            unique_together={("content_hash", "project", "language", "check")},
        ),
        migrations.AlterIndexTogether(
            name="check", index_together={("project", "language", "content_hash")}
        ),
    ]
