# Generated by Django 4.0.5 on 2022-06-22 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0009_rename_space_slug_subscription_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='name',
            field=models.CharField(default=0, max_length=256),
            preserve_default=False,
        ),
    ]
