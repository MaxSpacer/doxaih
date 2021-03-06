# Generated by Django 2.1.4 on 2019-01-15 13:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('image', models.ImageField(default=None, null=True, upload_to='event_images/')),
                ('description', models.TextField(blank=True, default=None, max_length=256, null=True)),
                ('content', tinymce.models.HTMLField(default=None, null=True, verbose_name='Content')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('publicated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='EducationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Категория курсов',
                'verbose_name_plural': 'Категории курсов',
            },
        ),
        migrations.AddField(
            model_name='education',
            name='category',
            field=models.ForeignKey(blank=True, default=None, max_length=64, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='educations.EducationCategory'),
        ),
    ]
