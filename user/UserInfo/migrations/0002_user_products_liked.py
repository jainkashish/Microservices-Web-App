# Generated by Django 3.1.4 on 2021-01-08 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserInfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='products_liked',
            field=models.IntegerField(default=0),
        ),
    ]
