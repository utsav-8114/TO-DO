# Generated by Django 5.2 on 2025-04-04 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tasks',
            new_name='Task',
        ),
    ]
