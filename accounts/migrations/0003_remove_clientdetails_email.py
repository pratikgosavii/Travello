# Generated by Django 3.0.2 on 2020-03-22 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200322_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientdetails',
            name='email',
        ),
    ]
