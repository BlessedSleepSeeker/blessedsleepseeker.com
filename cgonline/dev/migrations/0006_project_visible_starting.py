# Generated by Django 4.2.5 on 2023-09-23 15:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("dev", "0005_alter_project_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="visible_starting",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]