# Generated by Django 3.0.2 on 2020-03-31 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_clientdetails_gmail'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientdetails',
            name='city',
            field=models.CharField(default='gsh', max_length=50),
        ),
    ]
