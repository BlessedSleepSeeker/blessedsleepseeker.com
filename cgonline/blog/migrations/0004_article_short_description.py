# Generated by Django 4.2.5 on 2023-09-23 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_article_active_remove_article_language_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='short_description',
            field=models.TextField(default='bonjour'),
            preserve_default=False,
        ),
    ]
