# Generated by Django 3.0.11 on 2021-01-28 13:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('words', '0010_auto_20210128_0514'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='learned',
            unique_together={('user', 'word')},
        ),
    ]
