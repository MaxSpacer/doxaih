# Generated by Django 2.2 on 2019-06-02 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_order_session_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_session_key',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
    ]
