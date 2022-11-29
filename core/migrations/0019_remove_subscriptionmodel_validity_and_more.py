# Generated by Django 4.1.2 on 2022-11-29 05:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0018_subscriptionmodel_subscribermodel_payment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="subscriptionmodel",
            name="validity",
        ),
        migrations.AddField(
            model_name="subscribermodel",
            name="validity",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
