# Generated by Django 3.1.5 on 2021-04-27 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schema',
            name='simply',
        ),
        migrations.AlterField(
            model_name='schema',
            name='schema',
            field=models.JSONField(),
        ),
    ]