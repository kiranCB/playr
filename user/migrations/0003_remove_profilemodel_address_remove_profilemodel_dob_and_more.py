# Generated by Django 4.1.2 on 2022-11-03 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_addressmodel_locationmodel_profilemodel_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profilemodel",
            name="address",
        ),
        migrations.RemoveField(
            model_name="profilemodel",
            name="dob",
        ),
        migrations.DeleteModel(
            name="AddressModel",
        ),
    ]
