# Generated by Django 4.0.5 on 2022-06-22 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0010_subscription_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
