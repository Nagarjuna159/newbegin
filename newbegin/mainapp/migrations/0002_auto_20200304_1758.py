# Generated by Django 2.2 on 2020-03-04 12:28

from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_model',
            name='phone',
            field=models.IntegerField(validators=[mainapp.models.validate_phone]),
        ),
    ]
