# Generated by Django 3.2.18 on 2023-06-19 07:43

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_pf', '0021_auto_20230617_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headings',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='paragraph',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]