# Generated by Django 4.2.5 on 2023-09-27 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dev", "0007_project_release_alter_project_source"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="short_descriptionFR",
            field=models.TextField(default="1"),
            preserve_default=False,
        ),
    ]
