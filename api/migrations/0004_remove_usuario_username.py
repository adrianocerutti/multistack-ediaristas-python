# Generated by Django 3.2.8 on 2021-11-01 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20211027_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='username',
        ),
    ]