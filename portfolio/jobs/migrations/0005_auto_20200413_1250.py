# Generated by Django 3.0.5 on 2020-04-13 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_projects'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]
