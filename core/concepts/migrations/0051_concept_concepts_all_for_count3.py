# Generated by Django 4.1.3 on 2023-02-01 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concepts', '0050_remove_concept_concepts_public_cond_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='concept',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False), ('id', models.F('versioned_object_id'))), fields=['parent_id', 'is_active', 'retired', 'id', 'versioned_object_id'], name='concepts_all_for_count3'),
        ),
    ]
