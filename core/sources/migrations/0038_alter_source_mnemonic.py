# Generated by Django 4.1.7 on 2023-04-13 11:13

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0037_remove_source_sources_is_late_672be3_idx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='mnemonic',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(regex=re.compile('^[a-zA-Z0-9\\-\\.\\_\\@]+$'))]),
        ),
    ]
