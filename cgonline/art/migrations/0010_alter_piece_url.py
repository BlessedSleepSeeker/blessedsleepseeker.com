# Generated by Django 4.2.5 on 2023-09-23 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("art", "0009_alter_piece_album_alter_piece_scaling_method"),
    ]

    operations = [
        migrations.AlterField(
            model_name="piece",
            name="url",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
