# Generated by Django 2.2 on 2020-06-03 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_remove_productimage_is_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='order_sort',
            field=models.PositiveSmallIntegerField(blank=True, default=None, null=True, verbose_name='Порядок сортировки'),
        ),
    ]
