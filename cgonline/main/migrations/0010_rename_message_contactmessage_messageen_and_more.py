# Generated by Django 4.2.5 on 2023-09-28 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0009_rename_link_contactlink_direct_link_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contactmessage",
            old_name="message",
            new_name="messageEN",
        ),
        migrations.AddField(
            model_name="contactmessage",
            name="messageFR",
            field=models.TextField(default="o"),
            preserve_default=False,
        ),
    ]
