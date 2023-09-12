# Generated by Django 4.2.5 on 2023-09-12 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContactOption",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(blank=True, max_length=2000)),
                ("twitter", models.URLField(blank=True, max_length=2000)),
                ("instagram", models.URLField(blank=True, max_length=2000)),
                ("discord", models.URLField(blank=True, max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name="FAQuestion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.CharField(max_length=2000)),
                ("answer", models.TextField()),
                ("picture", models.ImageField(blank=True, upload_to="questions/")),
            ],
        ),
        migrations.CreateModel(
            name="Friend",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=2000)),
                ("picture", models.ImageField(blank=True, upload_to="friends/")),
                ("link", models.URLField(blank=True, max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name="Presentation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
                ("picture", models.ImageField(blank=True, upload_to="aboutme/")),
            ],
        ),
    ]