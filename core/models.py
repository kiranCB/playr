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
class CategoryModel(models.Model):
    name=models.CharField(max_length=64)
    parent=models.ForeignKey("self",on_delete=models.SET_NULL, null=True, blank= True)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

# Artist Model
class ArtistModel(models.Model):
    name=models.CharField(max_length=64)
    country=models.CharField(max_length=64)
    # songs=models.
    parent=models.ForeignKey("self",on_delete=models.SET_NULL, null=True, blank= True)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

# Song Model
class SongModel(models.Model):    
    name=models.CharField(max_length=64)
    # artist=models.ManyToOneRel(ArtistModel)
    description=models.TextField(max_length=500)#description
    image = models.ImageField(upload_to="product/image/", default="default/default.png")
    category=models.ManyToManyField(CategoryModel)
    status = models.BooleanField(default=True)
    created_on=models.DateField(auto_now_add=True)
    updated_on=models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"

class PlaylistModel(models.Model):
    pass
class GenreModel(models.Model):
    pass
class LanguageModel(models.Model):
    pass



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

    pass

# Join Model

class JoinModel(models.Model):
    pass

# ===================Room Model End=======================#

