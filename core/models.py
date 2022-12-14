from django.db import models
from django.conf import settings

USER = settings.AUTH_USER_MODEL


class TimeStamp(models.Model):
    status = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    class Meta:
        abstract = True


# Feedback model
class FeedbackModel(TimeStamp, models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    subject = models.CharField(max_length=164)
    message = models.TextField(max_length=500)

    def __str__(self) -> str:
        return f"{self.subject}"


# ===================Music model start=====================#

# Category Model
class GenreModel(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to="genre/image/", default="default/default.png")

    def __str__(self):
        return f"{self.name}"


# Language Model
class LanguageModel(TimeStamp, models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


# Song Model
class SongModel(TimeStamp, models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=500, default="None")  # description
    image = models.ImageField(upload_to="songs/image/", default="default/default.png")
    genre = models.ManyToManyField(GenreModel)
    song = models.FileField(upload_to="songs/mp3", default="default/default.png")
    language = models.ManyToManyField(LanguageModel)

    def __str__(self) -> str:
        return f"{self.name}"


# Artist Model
class ArtistModel(models.Model):
    name = models.CharField(max_length=64)
    nationality = models.CharField(max_length=64)
    songs = models.ManyToManyField(SongModel)
    image = models.ImageField(upload_to="songs/artist/", default="default/default.png")

    def __str__(self):
        return f"{self.name}"


# Playlist Model
class PlaylistModel(TimeStamp, models.Model):
    name = models.CharField(max_length=64, default=None)
    description = models.TextField(max_length=500, default="none")  # description
    image = models.ImageField(
        upload_to="playlist/image/", default="default/default.png"
    )
    user = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"


class FavouriteListModel(TimeStamp, models.Model):
    name = models.CharField(max_length=64, default="Favorite List")
    user = models.ForeignKey(USER, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"


class FavouriteItemModel(TimeStamp, models.Model):
    favourite_list = models.ForeignKey(FavouriteListModel, on_delete=models.CASCADE)
    song = models.ForeignKey(SongModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.song}"


# ===================Music Model End======================#

# ===================Room Model Start=====================#

# host model
class HostModel(TimeStamp, models.Model):
    name = models.CharField(max_length=64)
    room_name = models.CharField(max_length=64)
    accessibility = models.BooleanField(default=True)
    password = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.name}"


# Join Model


class JoinModel(TimeStamp, models.Model):
    room_name = models.CharField(max_length=64, default=None)
    password = models.CharField(max_length=20, default=None)
    accessibility = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.room_name}"


class SubscriptionModel(TimeStamp, models.Model):
    class SubscriptionTypeChoice(models.TextChoices):
        MONTH = "month", "Monthly"
        YEAR = "year", "Yearly"

    cost = models.FloatField()
    type = models.CharField(
        max_length=5,
        choices=SubscriptionTypeChoice.choices,
        default=SubscriptionTypeChoice.MONTH,
    )

    def __str__(self):
        name = (
            f"{self.cost}/{(self.SubscriptionTypeChoice(self.type).name).capitalize()}"
        )
        return name


class SubscriberModel(TimeStamp, models.Model):
    user = models.OneToOneField(USER, on_delete=models.CASCADE)
    subscription = models.OneToOneField(
        SubscriptionModel, on_delete=models.SET_NULL, null=True, blank=True
    )
    auto_renew = models.BooleanField(default=True)
    validity = models.DateField()

    def __str__(self):
        name = f"{self.user} {self.subscription}"
        return name


# ===================Room Model End=======================#
class Payment(TimeStamp, models.Model):
    class PaymentStatusChoices:
        pending = "pending"
        completed = "completed"
        failed = "failed"

    PAYMENT_STATUS_CHOICES = (
        ("Pending", PaymentStatusChoices.pending),
        ("Completed", PaymentStatusChoices.completed),
        ("Failed", PaymentStatusChoices.failed),
    )
    status = models.CharField(
        max_length=16,
        choices=PAYMENT_STATUS_CHOICES,
        default=PaymentStatusChoices.pending,
    )
    subscriber = models.ForeignKey(SubscriberModel, on_delete=models.CASCADE)
    mode = models.CharField(max_length=50, null=True, blank=True)
    razorpay_order_id = models.CharField(max_length=256)
    razorpay_payment_id = models.CharField(max_length=256)
    razorpay_amount = (models.FloatField(),)
    razorpay_currency = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.razorpay_order_id} - ({self.status})"
