# Generated by Django 3.2 on 2021-04-24 08:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catelog', '0002_lead_owner'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lead',
            new_name='Catelog',
        ),
    ]
