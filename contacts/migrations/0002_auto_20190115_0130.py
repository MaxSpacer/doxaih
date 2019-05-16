# Generated by Django 2.1.4 on 2019-01-14 22:30

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('content', tinymce.models.HTMLField(verbose_name='Content')),
                ('order_render', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Страница Contacts',
                'verbose_name_plural': '',
            },
        ),
        migrations.DeleteModel(
            name='Aboutus',
        ),
    ]