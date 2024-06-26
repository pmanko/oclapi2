# Generated by Django 4.1.1 on 2022-12-05 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('concepts', '0041_rename_descriptions_concept_descriptions_old_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conceptdescription',
            name='concept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='descriptions', to='concepts.concept'),
        ),
        migrations.AlterField(
            model_name='localizedtext',
            name='concept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='names', to='concepts.concept'),
        ),
    ]
