# Generated by Django 4.2.5 on 2023-09-24 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dev", "0006_project_visible_starting"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="release",
            field=models.FileField(blank=True, upload_to="upload/dev/releases/"),
        ),
        migrations.AlterField(
            model_name="project",
            name="source",
            field=models.FileField(blank=True, upload_to="upload/dev/sources/"),
        ),
    ]
