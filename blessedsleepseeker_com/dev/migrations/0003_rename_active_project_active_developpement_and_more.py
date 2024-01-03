# Generated by Django 4.2.5 on 2023-09-23 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dev", "0002_alter_project_source_alter_project_vignette"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="active",
            new_name="active_developpement",
        ),
        migrations.RenameField(
            model_name="project",
            old_name="name",
            new_name="title",
        ),
        migrations.RemoveField(
            model_name="project",
            name="languages",
        ),
        migrations.RemoveField(
            model_name="project",
            name="vignette",
        ),
        migrations.AddField(
            model_name="project",
            name="miniature",
            field=models.ImageField(default="a", upload_to="upload/dev/"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="project",
            name="short_description",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="project",
            name="source",
            field=models.FileField(upload_to="upload/dev/sources/"),
        ),
    ]