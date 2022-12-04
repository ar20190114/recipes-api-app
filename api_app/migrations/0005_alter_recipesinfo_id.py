# Generated by Django 4.1.3 on 2022-12-04 03:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0004_alter_recipesinfo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipesinfo',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
