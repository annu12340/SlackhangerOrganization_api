# Generated by Django 3.1.5 on 2021-04-27 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0003_auto_20210427_1302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schema',
            old_name='type',
            new_name='dress_type',
        ),
    ]