# Generated by Django 3.0.6 on 2020-05-15 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0054_auto_20200515_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientdetails',
            name='agent_address',
            field=models.CharField(default='not define', max_length=50),
        ),
        migrations.AddField(
            model_name='clientdetails',
            name='agentnumber',
            field=models.CharField(default='8237377298', max_length=10),
        ),
        migrations.AddField(
            model_name='clientdetails',
            name='dec',
            field=models.TextField(default='hdhfzsds'),
        ),
        migrations.AddField(
            model_name='clientdetails',
            name='image',
            field=models.ImageField(default='picc', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='clientdetails',
            name='price',
            field=models.IntegerField(default=5654),
        ),
    ]
