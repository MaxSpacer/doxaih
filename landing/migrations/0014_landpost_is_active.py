# Generated by Django 2.2 on 2019-06-10 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0013_auto_20190610_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='landpost',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
