# Generated by Django 4.1.7 on 2023-04-13 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0019_alter_organization_uri'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='organization',
            name='organizatio_public__2d2963_idx',
        ),
    ]