from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
     # core urls
     path("", views.HomeView.as_view(), name="home"),
     path("about_us/", views.AboutUsView.as_view(), name="about_us"),
     
     path("player/<int:pk>/play/", views.PlayerView.as_view(), name="player"),
     path("playlist/", views.PlaylistView.as_view(), name="playlist"),
     path("genre/", views.GenreView.as_view(), name="genre"),
     path("queue/<int:pk>/queue", views.QueueView.as_view(), name="queue"),
     path("playlist/detail", views.PlaylistDetailView.as_view(), name="playlist_detail"),
     path("genre/<int:pk>/detail", views.GenreDetailView.as_view(), name="genre_detail"),
    #  room
     path("host/", views.HostView.as_view(), name="host"),
     path("host/<int:pk>/room", views.HostDetailView.as_view(), name="hostroom"),
     path("join/", views.JoinView.as_view(), name="join"),
     # feedback url
     path("feedback/create", views.FeedbackCreateView.as_view(), name="feedback"),
     path("feedback/list/", views.FeedbackListView.as_view(), name="feedback_list"),
     path("feedback/<int:pk>/detail/",views.FeedbackDetailView.as_view(),name="feedback_detail"),
     path("feedback/<int:pk>/update/",views.FeedbackUpdateView.as_view(),name="feedback_update"),
     path("feedback/<int:pk>/delete/",views.FeedbackDeleteView.as_view(),name="feedback_delete"),
     path("api/song/", views.SongsAPIView.as_view(), name="api_song"),
       # favourite
     path("favourite/", views.FavouriteView.as_view(), name="favourite"),
     path("song/<int:pk>/add/", views.AddToFavouriteView.as_view(), name="add_to_favorite"),
    #  Subscription
    path("user/subcription/", views.SubcribeView.as_view(), name="subscribe_user"),
    path("user/subscription/payment/", views.SubscriptionPaymentView.as_view(), name="payment"),
    # search
    path("song/search/",views.SongSearchView.as_view(),name="song_search"),
]
