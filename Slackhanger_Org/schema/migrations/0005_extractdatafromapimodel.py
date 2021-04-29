# Generated by Django 3.1.5 on 2021-04-29 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schema', '0004_auto_20210427_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtractDataFromAPIModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dress_type', models.CharField(max_length=100)),
                ('schema_format', models.JSONField()),
                ('organizationID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
