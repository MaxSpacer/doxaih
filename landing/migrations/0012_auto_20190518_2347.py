# Generated by Django 2.2 on 2019-05-18 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0011_auto_20190518_2337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='callmecontact',
            old_name='contact_phone',
            new_name='customer_phone',
        ),
        migrations.RenameField(
            model_name='mainformcontact',
            old_name='contact_email',
            new_name='customer_email',
        ),
        migrations.RenameField(
            model_name='mainformcontact',
            old_name='contact_phone',
            new_name='customer_phone',
        ),
    ]
