# Generated by Django 4.2 on 2023-04-27 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0008_customer_vehicle_size_vehicle_rental_rate_rental'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='date_created',
            field=models.DateField(),
        ),
    ]
