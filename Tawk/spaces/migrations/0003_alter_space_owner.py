# Generated by Django 4.0.5 on 2022-06-19 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spaces', '0002_space_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='owner',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
