# Generated by Django 3.2.18 on 2023-05-24 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_pf', '0002_skill_skillcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skillcategory',
            name='skill',
        ),
        migrations.AddField(
            model_name='skill',
            name='category',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='my_pf.skillcategory'),
            preserve_default=False,
        ),
    ]
