# Generated by Django 4.2.5 on 2023-09-13 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dev", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="source",
            field=models.FileField(upload_to="upload/dev/sources"),
        ),
        migrations.AlterField(
            model_name="project",
            name="vignette",
            field=models.ImageField(blank=True, upload_to="upload/dev"),
        ),
    ]