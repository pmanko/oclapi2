# Generated by Django 4.2.4 on 2024-03-22 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('url_registry', '0004_alter_urlregistry_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlregistry',
            name='repo_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='urlregistry',
            name='repo_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]