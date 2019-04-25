# Generated by Django 2.1.7 on 2019-04-24 14:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sprayer', '0009_owner_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]