# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-27 14:06

from django.db import migrations, models

import weblate.utils.validators


class Migration(migrations.Migration):

    dependencies = [("weblate_auth", "0003_auto_20180724_1120")]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                max_length=190,
                null=True,
                unique=True,
                validators=[weblate.utils.validators.validate_email],
                verbose_name="E-mail",
            ),
        )
    ]
