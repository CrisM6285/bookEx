# Generated by Django 3.1.5 on 2021-05-01 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookMng', '0017_announcement_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='post_date',
            field=models.DateField(auto_now=True),
        ),
    ]
