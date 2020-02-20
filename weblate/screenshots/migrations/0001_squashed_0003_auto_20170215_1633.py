# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-21 13:08

import django.db.models.deletion
from django.db import migrations, models

import weblate.screenshots.fields


class Migration(migrations.Migration):

    replaces = [
        ("screenshots", "0001_initial"),
        ("screenshots", "0002_auto_20170215_0849"),
        ("screenshots", "0003_auto_20170215_1633"),
    ]

    initial = True

    dependencies = [("trans", "0074_auto_20170209_1412")]

    operations = [
        migrations.CreateModel(
            name="Screenshot",
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
                (
                    "name",
                    models.CharField(max_length=200, verbose_name="Screenshot name"),
                ),
                (
                    "image",
                    weblate.screenshots.fields.ScreenshotField(
                        help_text="Upload JPEG or PNG images up to 2000x2000 pixels.",
                        upload_to="screenshots/",
                        verbose_name="Image",
                    ),
                ),
                (
                    "component",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="trans.Component",
                    ),
                ),
                (
                    "sources",
                    models.ManyToManyField(
                        blank=True, related_name="screenshots", to="trans.Source"
                    ),
                ),
            ],
            options={"ordering": ["name"]},
        )
    ]
