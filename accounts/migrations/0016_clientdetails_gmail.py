# Generated by Django 3.0.2 on 2020-03-24 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20200324_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientdetails',
            name='gmail',
            field=models.CharField(default='vdx', max_length=50),
        ),
    ]