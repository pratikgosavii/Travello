# Generated by Django 3.0.2 on 2020-05-10 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0050_clientdetails_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdetails',
            name='code',
            field=models.CharField(default='gsh', max_length=50),
        ),
    ]
