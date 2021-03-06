# Generated by Django 3.0.2 on 2020-04-07 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0008_remove_destination_destinationuser'),
        ('accounts', '0039_auto_20200406_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yourtrips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yourtrips', to='travello.Destination')),
                ('trips', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yourtrips', to='accounts.clientdetails')),
            ],
        ),
    ]
