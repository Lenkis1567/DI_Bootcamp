# Generated by Django 4.2 on 2023-04-28 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0010_alter_rental_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='rental_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='rental',
            name='return_date',
            field=models.DateField(),
        ),
    ]