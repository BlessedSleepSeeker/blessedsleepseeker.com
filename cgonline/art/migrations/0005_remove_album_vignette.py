# Generated by Django 4.2.5 on 2023-09-18 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("art", "0004_piece_url"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="album",
            name="vignette",
        ),
    ]
