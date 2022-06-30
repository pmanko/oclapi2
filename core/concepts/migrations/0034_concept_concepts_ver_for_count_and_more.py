# Generated by Django 4.0.4 on 2022-06-24 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concepts', '0033_remove_concept_concepts_updated_6490d8_idx_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='concept',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False)), fields=['is_active'], name='concepts_ver_for_count'),
        ),
        migrations.AddIndex(
            model_name='concept',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False)), fields=['-updated_at'], name='concepts_ver_for_sort'),
        ),
    ]