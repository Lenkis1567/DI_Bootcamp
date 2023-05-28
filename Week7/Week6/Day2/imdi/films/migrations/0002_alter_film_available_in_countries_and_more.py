# Generated by Django 4.2 on 2023-05-03 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='available_in_countries',
            field=models.ManyToManyField(related_name='country_availible', to='films.country'),
        ),
        migrations.AlterField(
            model_name='film',
            name='director_v',
            field=models.ManyToManyField(related_name='dir_films', to='films.director'),
        ),
    ]
