# Generated by Django 3.0.11 on 2021-01-26 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0005_word_definition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='definition',
        ),
    ]
