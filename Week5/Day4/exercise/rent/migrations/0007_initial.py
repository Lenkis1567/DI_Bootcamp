# Generated by Django 4.2 on 2023-04-27 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rent', '0006_delete_customer_remove_rental_rate_vehicle_size_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
            ],
        ),
    ]
