# Generated by Django 4.1.2 on 2022-11-15 04:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_genremodel_created_on_genremodel_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="artistmodel",
            name="songs",
            field=models.ManyToManyField(to="core.songmodel"),
        ),
        migrations.AddField(
            model_name="joinmodel",
            name="accessibility",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="joinmodel",
            name="password",
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name="joinmodel",
            name="room_name",
            field=models.CharField(default=None, max_length=64),
        ),
        migrations.AddField(
            model_name="languagemodel",
            name="name",
            field=models.CharField(default="English", max_length=64),
        ),
        migrations.AddField(
            model_name="playlistmodel",
            name="created_on",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="playlistmodel",
            name="description",
            field=models.TextField(default="none", max_length=500),
        ),
        migrations.AddField(
            model_name="playlistmodel",
            name="image",
            field=models.ImageField(
                default="default/default.png", upload_to="product/image/"
            ),
        ),
        migrations.AddField(
            model_name="playlistmodel",
            name="name",
            field=models.CharField(default=None, max_length=64),
        ),
        migrations.AddField(
            model_name="playlistmodel",
            name="status",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="playlistmodel",
            name="updated_on",
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name="songmodel",
            name="language",
            field=models.ManyToManyField(to="core.languagemodel"),
        ),
        migrations.AlterField(
            model_name="songmodel",
            name="description",
            field=models.TextField(default="None", max_length=500),
        ),
    ]