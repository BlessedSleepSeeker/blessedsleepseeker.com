# Generated by Django 4.2.5 on 2023-09-22 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("art", "0008_alter_piece_album_alter_piece_scaling_method"),
    ]

    operations = [
        migrations.AlterField(
            model_name="piece",
            name="album",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="art.album"
            ),
        ),
        migrations.AlterField(
            model_name="piece",
            name="scaling_method",
            field=models.CharField(
                choices=[
                    ("auto", "auto"),
                    ("crisp-edges", "crisp-edges"),
                    ("smooth", "smooth"),
                    ("pixelated", "pixelated"),
                ],
                default="pixelated",
                max_length=20,
            ),
        ),
    ]