from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
     # core urls
     path("", views.HomeView.as_view(), name="home"),
     path("about_us/", views.AboutUsView.as_view(), name="about_us"),
     path("profile/", views.ProfileView.as_view(), name="profile"),


     path("player/", views.PlayerView.as_view(), name="player"),
     path("favourite/", views.FavouriteView.as_view(), name="favourite"),
     path("playlist/", views.PlaylistView.as_view(), name="playlist"),
     path("queue/", views.QueueView.as_view(), name="queue"),
     path("host/", views.HostView.as_view(), name="host"),
     path("join/", views.JoinView.as_view(), name="join"),
     path("genre/", views.GenreView.as_view(), name="genre"),
     # feedback url
     path("feedback/create", views.FeedbackCreateView.as_view(), name="feedback"),
    
]
