# Generated by Django 2.1.7 on 2019-03-29 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('service', models.CharField(max_length=128)),
                ('image', models.ImageField(default=None, null=True, upload_to='team_images/')),
                ('order_render', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Участник команды',
                'verbose_name_plural': 'Участники команды',
            },
        ),
    ]
