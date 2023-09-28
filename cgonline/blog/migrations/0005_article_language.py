# Generated by Django 4.2.5 on 2023-09-27 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_article_short_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="language",
            field=models.CharField(
                choices=[("fr", "Francais"), ("en-uk", "English")],
                default="a",
                max_length=5,
            ),
            preserve_default=False,
        ),
    ]