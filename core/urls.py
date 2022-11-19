from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
     # core urls
     path("", views.HomeView.as_view(), name="home"),
     path("about_us/", views.AboutUsView.as_view(), name="about_us"),
     
     path("player/<int:pk>/play/", views.PlayerView.as_view(), name="player"),
     path("favourite/", views.FavouriteView.as_view(), name="favourite"),
     path("playlist/", views.PlaylistView.as_view(), name="playlist"),
     path("queue/", views.QueueView.as_view(), name="queue"),
     path("host/", views.HostView.as_view(), name="host"),
     path("join/", views.JoinView.as_view(), name="join"),
     path("genre/", views.GenreView.as_view(), name="genre"),
     path("genre/detail", views.GenreDetailView.as_view(), name="genre_detail"),
     path("playlist/detail", views.PlaylistDetailView.as_view(), name="playlist_detail"),
     # feedback url
     path("feedback/create", views.FeedbackCreateView.as_view(), name="feedback"),
     path("feedback/list/", views.FeedbackListView.as_view(), name="feedback_list"),
     path("feedback/<int:pk>/detail/",views.FeedbackDetailView.as_view(),name="feedback_detail"),
     path("feedback/<int:pk>/update/",views.FeedbackUpdateView.as_view(),name="feedback_update"),
     path("feedback/<int:pk>/delete/",views.FeedbackDeleteView.as_view(),name="feedback_delete"),
    
]
