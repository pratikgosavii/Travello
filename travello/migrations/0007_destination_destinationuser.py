# Generated by Django 3.0.2 on 2020-04-05 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0033_remove_clientdetails_destinationuser'),
        ('travello', '0006_remove_destination_destination_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='destinationuser',
            field=models.ManyToManyField(to='accounts.clientdetails'),
        ),
    ]
