# Generated by Django 3.0.2 on 2020-03-22 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdetails',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
