# Generated by Django 3.0.2 on 2020-02-03 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='dec',
            field=models.TextField(default='hdhfzsds'),
        ),
        migrations.AddField(
            model_name='destination',
            name='image',
            field=models.ImageField(default='picc', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='destination',
            name='name',
            field=models.CharField(default='vdx', max_length=10),
        ),
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='destination',
            name='offer',
            field=models.BooleanField(default=False),
        ),
    ]