# Generated by Django 4.1.2 on 2022-11-25 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0013_playlistmodel_user_favouritemodel"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="favouritemodel",
            name="name",
        ),
        migrations.RemoveField(
            model_name="genremodel",
            name="parent",
        ),
        migrations.AlterField(
            model_name="favouritemodel",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="playlistmodel",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="FavouriteSongModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.BooleanField(default=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                (
                    "favourite",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.favouritemodel",
                    ),
                ),
                (
                    "song",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.songmodel"
                    ),
                ),
            ],
        ),
    ]
