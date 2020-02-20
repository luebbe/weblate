# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-11 14:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("trans", "0003_remove_translation_commit_message")]

    operations = [
        migrations.AddField(
            model_name="project",
            name="use_shared_tm",
            field=models.BooleanField(
                default=settings.DEFAULT_SHARED_TM,
                help_text="Uses and contributes to the pool of shared translations between projects.",
                verbose_name="Use shared translation memory",
            ),
        )
    ]
