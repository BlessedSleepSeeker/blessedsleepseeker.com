# Generated by Django 4.2.5 on 2023-09-19 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_contactlink_contactmessage_delete_contactoption"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactlink",
            name="link",
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name="contactlink",
            name="title",
            field=models.CharField(max_length=200),
        ),
    ]
