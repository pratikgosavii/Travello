# Generated by Django 3.0.2 on 2020-03-24 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200324_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientdetails',
            name='occupation',
            field=models.CharField(default='vdx', max_length=50),
        ),
        migrations.AddField(
            model_name='clientdetails',
            name='status',
            field=models.CharField(default='vdx', max_length=50),
        ),
    ]
