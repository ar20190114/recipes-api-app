# Generated by Django 4.1.3 on 2022-12-04 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipesinfo',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
