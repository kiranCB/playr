from django.contrib import admin
from core import models

admin.site.register(models.FeedbackModel)
admin.site.register(models.GenreModel)
admin.site.register(models.SongModel)