# Generated by Django 5.0.3 on 2024-04-01 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='panel',
            name='display_image',
            field=models.TextField(blank=True, null=True),
        ),
    ]
