# Generated by Django 3.0.2 on 2020-05-06 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0046_remove_clientdetails_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientdetails',
            name='mode',
            field=models.CharField(default='not define', max_length=50),
        ),
        migrations.AddField(
            model_name='clientdetails',
            name='source',
            field=models.CharField(default='not define', max_length=50),
        ),
    ]
