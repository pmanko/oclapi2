# Generated by Django 4.2.4 on 2023-12-30 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mappings', '0050_mapping_mappings_latest'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='mapping',
            index=models.Index(condition=models.Q(('id', models.F('versioned_object_id'))), fields=['from_concept', 'parent_id'], name='direct_mappings'),
        ),
    ]
