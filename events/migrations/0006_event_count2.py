# Generated by Django 3.0.3 on 2021-05-23 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_register_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='count2',
            field=models.IntegerField(null=True),
        ),
    ]
