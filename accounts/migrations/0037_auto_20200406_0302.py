# Generated by Django 3.0.2 on 2020-04-05 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0036_clientdetails_destination'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientdetails',
            old_name='cityuser',
            new_name='name',
        ),
    ]
