# Generated by Django 3.0.2 on 2020-04-05 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_auto_20200402_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientdetails',
            name='cityuser',
            field=models.CharField(default='not define', max_length=50),
        ),
    ]