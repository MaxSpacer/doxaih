# Generated by Django 2.1.7 on 2019-04-01 14:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0005_auto_20190206_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('image', models.ImageField(default=None, null=True, upload_to='investions_images/')),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('duration', models.IntegerField(default=0)),
                ('invites', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True, default=None, max_length=256, null=True)),
                ('is_disabled', models.BooleanField(default=False)),
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
            name='InvestionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Категория инвестиций',
                'verbose_name_plural': 'Категории инвестиций',
            },
        ),
        migrations.CreateModel(
            name='InvestionFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Формат инвестиций',
                'verbose_name_plural': 'Форматы инвестиций',
            },
        ),
        migrations.CreateModel(
            name='InvestionOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='имя')),
                ('customer_email', models.EmailField(blank=True, default=None, max_length=64, null=True, verbose_name='электронная почта')),
                ('customer_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, max_length=24, null=True, region=None, verbose_name='телефон +7XXXXXXXX')),
                ('is_emailed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('investion', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='investions.Investion')),
                ('referal', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='accounts.Profile')),
            ],
            options={
                'verbose_name': 'Заказ инвестиции',
                'verbose_name_plural': 'Заказы инвестиций',
            },
        ),
        migrations.CreateModel(
            name='InvestionPlanPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('content', tinymce.models.HTMLField(default=None, null=True, verbose_name='Content')),
                ('order', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('investion', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='investions.Investion')),
            ],
            options={
                'verbose_name': 'Пункт плана инвестиции',
                'verbose_name_plural': 'Пункты плана инвестиции',
            },
        ),
        migrations.CreateModel(
            name='InvestionResultPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('content', tinymce.models.HTMLField(default=None, null=True, verbose_name='Content')),
                ('order', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('investion', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='investions.Investion')),
            ],
            options={
                'verbose_name': 'Результат инвестиции',
                'verbose_name_plural': 'Результаты инвестиции',
            },
        ),
        migrations.CreateModel(
            name='StatusInvestionOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(blank=True, default=None, max_length=24, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Статус заказа',
                'verbose_name_plural': 'Статусы заказа',
            },
        ),
        migrations.AddField(
            model_name='investionorder',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='investions.StatusInvestionOrder'),
        ),
        migrations.AddField(
            model_name='investion',
            name='category',
            field=models.ForeignKey(blank=True, default=None, max_length=64, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='investions.InvestionCategory'),
        ),
        migrations.AddField(
            model_name='investion',
            name='format',
            field=models.ForeignKey(blank=True, default=None, max_length=64, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='investions.InvestionFormat'),
        ),
    ]