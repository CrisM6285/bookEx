# Generated by Django 3.1.5 on 2021-04-14 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookMng', '0003_auto_20210413_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='userName',
            field=models.CharField(max_length=200),
        ),
    ]
