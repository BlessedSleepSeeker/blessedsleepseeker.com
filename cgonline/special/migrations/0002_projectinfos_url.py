# Generated by Django 4.2.5 on 2023-09-21 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("special", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="projectinfos",
            name="url",
            field=models.CharField(default="sci-bi", max_length=200),
            preserve_default=False,
        ),
    ]
