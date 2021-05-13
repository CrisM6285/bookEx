# Generated by Django 3.1.5 on 2021-04-19 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookMng', '0006_auto_20210413_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('the_search', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='wish',
            name='bookName',
            field=models.CharField(max_length=200, verbose_name='Book Name'),
        ),
    ]