# Generated by Django 2.2.13 on 2020-10-04 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20201004_1856'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='imortant',
            new_name='important',
        ),
    ]
