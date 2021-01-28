# Generated by Django 3.0.11 on 2021-01-28 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('words', '0009_learned'),
    ]

    operations = [
        migrations.AddField(
            model_name='learned',
            name='user',
            field=models.ForeignKey(default=17, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='learned',
            name='word',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='words.Word'),
            preserve_default=False,
        ),
    ]
