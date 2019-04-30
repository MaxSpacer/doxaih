# Generated by Django 2.1.4 on 2019-01-15 14:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('educations', '0003_remove_education_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='educationimage',
            name='education',
        ),
        migrations.AddField(
            model_name='education',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='educations_images/'),
        ),
        migrations.DeleteModel(
            name='EducationImage',
        ),
    ]
