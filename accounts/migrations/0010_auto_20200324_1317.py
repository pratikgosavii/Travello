# Generated by Django 3.0.2 on 2020-03-24 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200324_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientdetails',
            name='last_name',
            field=models.CharField(default='vdx', max_length=50),
        ),
        migrations.AddField(
            model_name='clientdetails',
            name='middle_name',
            field=models.CharField(default='vdx', max_length=50),
        ),
    ]
