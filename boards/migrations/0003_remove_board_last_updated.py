# Generated by Django 2.1.3 on 2018-11-07 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_board_last_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='last_updated',
        ),
    ]
