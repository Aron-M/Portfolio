# Generated by Django 3.2.18 on 2023-06-22 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_pf', '0026_auto_20230621_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='extra_info',
            field=models.CharField(default='lorem lorem lorem ipsum', max_length=500),
            preserve_default=False,
        ),
    ]
