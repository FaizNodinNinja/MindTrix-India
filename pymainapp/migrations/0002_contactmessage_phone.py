# Generated by Django 5.1.6 on 2025-02-28 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pymainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='phone',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
