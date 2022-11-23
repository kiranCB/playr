from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()

#Feedback model
class FeedbackModel(models.Model):
    name=models.CharField(max_length=64)
    email=models.EmailField()
    subject=models.CharField(max_length=164)
    message=models.TextField(max_length=500)
    status=models.BooleanField(default=True)
    created_on=models.DateField(auto_now_add=True)
    updated_on=models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.subject}"

# ===================Music model start=====================#

# Category Model
class GenreModel(models.Model):
    name=models.CharField(max_length=64)
    parent=models.ForeignKey("self",on_delete=models.SET_NULL, null=True, blank= True)
    image = models.ImageField(upload_to="genre/image/", default="default/default.png")
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

# Language Model
class LanguageModel(models.Model):
    name=models.CharField(max_length=64)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
    
# Song Model
class SongModel(models.Model):    
    name=models.CharField(max_length=64)
    description=models.TextField(max_length=500, default="None")#description
    image = models.ImageField(upload_to="songs/image/", default="default/default.png")
    genre=models.ManyToManyField(GenreModel)
    song=models.FileField(upload_to="songs/mp3", default="default/default.png")
    language=models.ManyToManyField(LanguageModel)
    status = models.BooleanField(default=True)
    created_on=models.DateField(auto_now_add=True)
    updated_on=models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"

# Artist Model
class ArtistModel(models.Model):
    name=models.CharField(max_length=64)
    nationality=models.CharField(max_length=64)
    songs=models.ManyToManyField(SongModel)
    image = models.ImageField(upload_to="songs/artist/", default="default/default.png")
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
         
    def __str__(self):
        return f"{self.name}"

# Playlist Model
class PlaylistModel(models.Model):
    name=models.CharField(max_length=64, default=None)
    description=models.TextField(max_length=500,default="none")#description
    image = models.ImageField(upload_to="playlist/image/", default="default/default.png")
    status = models.BooleanField(default=True)
    created_on=models.DateField(auto_now_add=True)
    updated_on=models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"





# ===================Music Model End======================#

# ===================Room Model Start=====================#

# host model
class HostModel(models.Model):
    name = models.CharField(max_length=64)
    room_name = models.CharField(max_length=64)
    accessibility = models.BooleanField(default=True)
    password = models.CharField(max_length =20)
    status = models.BooleanField(default=True)
    created_on=models.DateField(auto_now_add=True)
    updated_on=models.DateField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.name}"

# Join Model

class JoinModel(models.Model):
    room_name = models.CharField(max_length=64,default=None)
    password = models.CharField(max_length =20, default=None)
    accessibility = models.BooleanField(default=True)
    def __str__(self) -> str:
        return f"{self.room_name}"

    

# ===================Room Model End=======================#

