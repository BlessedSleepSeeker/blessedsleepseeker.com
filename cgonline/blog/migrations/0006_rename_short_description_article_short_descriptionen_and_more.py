# Generated by Django 4.2.5 on 2023-10-04 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_article_language"),
    ]

    operations = [
        migrations.RenameField(
            model_name="article",
            old_name="short_description",
            new_name="short_descriptionEN",
        ),
        migrations.AddField(
            model_name="article",
            name="short_descriptionFR",
            field=models.TextField(default="aaaa"),
            preserve_default=False,
        ),
    ]