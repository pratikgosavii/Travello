# Generated by Django 3.0.2 on 2020-03-24 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_clientdetails_gmail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientdetails',
            name='term',
        ),
    ]