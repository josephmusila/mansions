# Generated by Django 4.0.4 on 2022-05-22 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_clientmessages_property_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='usage',
            field=models.CharField(choices=[('Rent', 'Rent'), ('Sale', 'Sale')], max_length=100),
        ),
    ]