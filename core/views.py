from cgitb import html
from django import views
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views

from core import models as core_models
from core.forms import FeedbackForm

#============================ Core Views start ====================================#
class HomeView(views.TemplateView):
    template_name = "core/home.html"

class AboutUsView(views.TemplateView):
    template_name = "core/about_us.html"


    
#============================ Core Views end ======================================#


#===========================Feedback Cred start====================================#

# feedback create view
class FeedbackCreateView(views.CreateView):
    template_name = "core/feedback/feedback_create.html"
    model = core_models.FeedbackModel
    form_class = FeedbackForm
    success_url = reverse_lazy("core:home")

class FeedbackDeleteView(views.DeleteView):
    template_name = "core/feedback/delete_feedback.html"
    model = core_models.FeedbackModel
    success_url = reverse_lazy("core:feedback_list")

class FeedbackUpdateView(views.UpdateView):
    template_name = "core/feedback/update_feedback.html"
    model = core_models.FeedbackModel
    form_class = FeedbackForm
    success_url = reverse_lazy("core:feedback_list")

class FeedbackListView(views.ListView):
    template_name = "core/feedback/feedback_list.html"
    model = core_models.FeedbackModel
    context_object_name = "feedbacks"

# feedback detailview
class FeedbackDetailView(views.DetailView):
    template_name = "core/feedback/feedback_detail.html"
    model = core_models.FeedbackModel
    context_object_name = "feedback"




# ===========================Feedback Cred end======================================#

# ===========================Song Cred Start======================================#

class PlayerView(views.TemplateView):
    template_name = "core/player.html"

class FavouriteView(views.TemplateView):
    template_name = "core/favourites.html"

class GenreView(views.TemplateView):
    template_name = "core/genre.html"

class HostView(views.TemplateView):
    template_name = "core/host.html"

class JoinView(views.TemplateView):
    template_name = "core/join.html"

class PlaylistView(views.TemplateView):
    template_name = "core/playlist.html"

class QueueView(views.TemplateView):
    template_name = "core/queue.html"

class GenreDetailView(views.TemplateView):
    template_name = "core/genredetail.html"
class PlaylistDetailView(views.TemplateView):
    template_name = "core/playlistdetail.html"




# ===========================Song Cred End======================================#
