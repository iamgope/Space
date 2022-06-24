# Generated by Django 4.0.5 on 2022-06-24 08:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0018_alter_posts_options_alter_comment_commented_on_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='Post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='spaces.posts'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='commented_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 24, 13, 31, 21, 23835)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='published_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 24, 13, 31, 21, 21841)),
        ),
    ]