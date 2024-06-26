# Generated by Django 4.2.4 on 2023-12-21 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mappings', '0048_auto_20230912_0327'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='mapping',
            index=models.Index(condition=models.Q(('id', models.F('versioned_object_id')), ('retired', False), ('sort_weight__isnull', False)), fields=['from_concept_id', 'sort_weight', 'parent_id', 'map_type'], name='mappings_sort_weight_next'),
        ),
    ]
