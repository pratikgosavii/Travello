# Generated by Django 3.0.2 on 2020-04-13 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0045_auto_20200407_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientdetails',
            name='city',
        ),
    ]