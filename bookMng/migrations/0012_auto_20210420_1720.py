# Generated by Django 3.1.5 on 2021-04-21 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookMng', '0011_auto_20210420_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysearch',
            name='id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]
