# Generated by Django 4.2.13 on 2024-05-29 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opai', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ppt',
            name='ppt_modified',
            field=models.FileField(blank=True, upload_to='ppt_modified/'),
        ),
    ]