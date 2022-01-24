# Generated by Django 3.1.12 on 2021-08-30 06:34

import core.collections.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    dependencies = [
        ('concepts', '0017_auto_20210720_1000'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mappings', '0019_auto_20210720_1000'),
        ('collections', '0026_auto_20210728_0656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expansion',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('internal_reference_id', models.CharField(blank=True, max_length=255, null=True)),
                ('public_access', models.CharField(blank=True, choices=[('View', 'View'), ('Edit', 'Edit'), ('None', 'None')], default='View', max_length=16)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('extras', models.JSONField(blank=True, default=dict, null=True)),
                ('uri', models.TextField(blank=True, db_index=True, null=True)),
                ('logo_path', models.TextField(blank=True, null=True)),
                ('mnemonic', models.CharField(db_index=True, max_length=255, validators=[django.core.validators.RegexValidator(regex=re.compile('^[a-zA-Z0-9\\-\\.\\_\\@]+$'))])),
                ('parameters', models.JSONField(default=core.collections.models.default_expansion_parameters)),
                ('canonical_url', models.URLField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('collection_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expansions', to='collections.collection')),
                ('concepts', models.ManyToManyField(blank=True, related_name='expansion_set', to='concepts.Concept')),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='collections_expansion_related_created_by', related_query_name='collections_expansions_created_by', to=settings.AUTH_USER_MODEL)),
                ('mappings', models.ManyToManyField(blank=True, related_name='expansion_set', to='mappings.Mapping')),
                ('references', models.ManyToManyField(blank=True, related_name='expansion_set', to='collections.CollectionReference')),
                ('updated_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='collections_expansion_related_updated_by', related_query_name='collections_expansions_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'collection_expansions',
            },
        ),
        migrations.AddIndex(
            model_name='expansion',
            index=models.Index(fields=['mnemonic'], name='collection__mnemoni_321d79_idx'),
        ),
        migrations.AddIndex(
            model_name='expansion',
            index=models.Index(fields=['uri'], name='collection__uri_8b34e9_idx'),
        ),
        migrations.AddIndex(
            model_name='expansion',
            index=models.Index(fields=['-updated_at'], name='collection__updated_8a275c_idx'),
        ),
        migrations.AddIndex(
            model_name='expansion',
            index=models.Index(fields=['-created_at'], name='collection__created_b1404c_idx'),
        ),
        migrations.AddIndex(
            model_name='expansion',
            index=models.Index(fields=['is_active'], name='collection__is_acti_0eb63b_idx'),
        ),
        migrations.AddIndex(
            model_name='expansion',
            index=models.Index(fields=['public_access'], name='collection__public__ce3ef6_idx'),
        ),
    ]