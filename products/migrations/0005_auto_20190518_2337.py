# Generated by Django 2.2 on 2019-05-18 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_popular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='popular',
            field=models.BooleanField(default=False, verbose_name='Популярные товары'),
        ),
    ]