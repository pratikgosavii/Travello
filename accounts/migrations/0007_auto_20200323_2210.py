# Generated by Django 3.0.2 on 2020-03-23 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_clientdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientdetails',
            name='additionalinformation',
        ),
        migrations.RemoveField(
            model_name='clientdetails',
            name='code',
        ),
        migrations.RemoveField(
            model_name='clientdetails',
            name='country',
        ),
        migrations.RemoveField(
            model_name='clientdetails',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='clientdetails',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='clientdetails',
            name='occupation',
        ),
        migrations.RemoveField(
            model_name='clientdetails',
            name='people',
        ),
        migrations.RemoveField(
            model_name='clientdetails',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='clientdetails',
            name='place',
        ),
        migrations.RemoveField(
            model_name='clientdetails',
            name='status',
        ),
        migrations.RemoveField(
            model_name='clientdetails',
            name='street',
        ),
        migrations.RemoveField(
            model_name='clientdetails',
            name='zip',
        ),
    ]
