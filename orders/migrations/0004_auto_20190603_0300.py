# Generated by Django 2.2 on 2019-06-03 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_order_session_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinbasket',
            name='pb_in_cart',
            field=models.BooleanField(default=True, verbose_name='в корзине?'),
        ),
    ]
