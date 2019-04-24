# Generated by Django 2.1.7 on 2019-04-24 14:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sprayer', '0010_auto_20190424_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='uuid',
        ),
        migrations.AlterField(
            model_name='owner',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
