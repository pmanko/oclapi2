# Generated by Django 4.2.16 on 2025-03-18 02:12

from django.db import migrations


def update_api_rate_limit_plan(apps, schema_editor):
    UserRateLimit = apps.get_model('users', 'UserRateLimit')
    UserRateLimit.objects.update(rate_plan='standard')


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0032_alter_userratelimit_rate_plan'),
    ]

    operations = [
        migrations.RunPython(update_api_rate_limit_plan),
    ]
