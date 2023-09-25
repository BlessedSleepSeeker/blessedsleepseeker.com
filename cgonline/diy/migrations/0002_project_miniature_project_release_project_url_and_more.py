# Generated by Django 4.2.5 on 2023-09-25 07:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("diy", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="miniature",
            field=models.ImageField(default="a", upload_to="upload/dev/"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="project",
            name="release",
            field=models.FileField(blank=True, upload_to="upload/dev/releases/"),
        ),
        migrations.AddField(
            model_name="project",
            name="url",
            field=models.CharField(default="a", max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="project",
            name="visible_starting",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="project",
            name="source",
            field=models.FileField(blank=True, upload_to="upload/dev/sources/"),
        ),
    ]
