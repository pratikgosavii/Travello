# Generated by Django 3.0.2 on 2020-02-03 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_auto_20200204_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default='5654'),
        ),
    ]
