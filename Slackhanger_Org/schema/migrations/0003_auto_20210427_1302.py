# Generated by Django 3.1.5 on 2021-04-27 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0002_auto_20210427_1245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schema',
            old_name='owner',
            new_name='organization',
        ),
        migrations.RenameField(
            model_name='schema',
            old_name='schema',
            new_name='schema_format',
        ),
    ]
