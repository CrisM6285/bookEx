# Generated by Django 3.1.5 on 2021-04-21 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookMng', '0009_mysearch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysearch',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
