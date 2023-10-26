# Generated by Django 3.2.18 on 2023-05-24 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Headings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('big_header', models.CharField(max_length=100)),
                ('sub_header', models.CharField(max_length=100)),
                ('par1', models.CharField(max_length=300)),
                ('par2', models.CharField(max_length=300)),
                ('par3', models.CharField(max_length=300)),
                ('par4', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('residency', models.CharField(max_length=200)),
                ('languages', models.CharField(max_length=200)),
                ('studying', models.CharField(max_length=200)),
                ('flag_nationality', models.ImageField(blank=True, null=True, upload_to='flags/')),
                ('flag_residency', models.ImageField(blank=True, null=True, upload_to='flags/')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='project_images/')),
                ('description', models.CharField(max_length=200)),
                ('github_url', models.URLField()),
            ],
        ),
    ]