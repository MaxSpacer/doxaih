# Generated by Django 2.1.4 on 2019-01-14 22:15

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callmecontact',
            name='contact_name',
            field=models.CharField(default=None, max_length=32, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='callmecontact',
            name='contact_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='Телефон'),
        ),
    ]