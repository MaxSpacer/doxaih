# Generated by Django 2.2 on 2019-05-13 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20181115_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinbasket',
            name='pb_total_price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]
